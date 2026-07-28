import { ActionIcon, Group, Text, TextInput } from '@mantine/core'
import { IconChevronDown, IconChevronUp, IconSearch, IconX } from '@tabler/icons-react'
import { useEffect, useRef, useState } from 'react'
import ReactJson, { ReactJsonViewProps } from 'react-json-view'
import { useJsonSearchModalContext } from './context'

export { default as SearchableJsonModal } from './SearchableJsonModal'

const HIGHLIGHT_ALL = 'json-search'
const HIGHLIGHT_CURRENT = 'json-search-current'

function collectMatchRanges(root: HTMLElement, query: string): Range[] {
  if (!query) return []
  const needle = query.toLowerCase()
  const ranges: Range[] = []
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT)
  let node: Node | null
  while ((node = walker.nextNode())) {
    const haystack = (node.textContent ?? '').toLowerCase()
    let from = 0
    for (;;) {
      const idx = haystack.indexOf(needle, from)
      if (idx === -1) break
      const range = new Range()
      range.setStart(node, idx)
      range.setEnd(node, idx + needle.length)
      ranges.push(range)
      from = idx + needle.length
    }
  }
  return ranges
}

// Drop-in replacement for `ReactJson` with a search toolbar, since Electron has no
// native Ctrl-F find bar. Highlights are drawn via the CSS Custom Highlight API so
// they never touch the DOM nodes react-json-view itself renders/reconciles. Render
// inside a SearchableJsonModal so Ctrl-F reaches this component.
export default function SearchableJsonView(props: ReactJsonViewProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const isHoveredRef = useRef(false)
  const rangesRef = useRef<Range[]>([])
  const searchModalCtx = useJsonSearchModalContext()

  const [isOpen, setIsOpen] = useState(false)
  const [query, setQuery] = useState('')
  const [debouncedQuery, setDebouncedQuery] = useState('')
  const [matchCount, setMatchCount] = useState(0)
  const [currentIndex, setCurrentIndex] = useState(0)

  const close = (): void => {
    setIsOpen(false)
    setQuery('')
  }

  useEffect(() => {
    if (!searchModalCtx) return
    return searchModalCtx.register({
      open: () => {
        setIsOpen(true)
        requestAnimationFrame(() => {
          inputRef.current?.focus()
          inputRef.current?.select()
        })
      },
      isHovered: () => isHoveredRef.current
    })
  }, [searchModalCtx])

  useEffect(() => {
    const timeout = setTimeout(() => setDebouncedQuery(query), 150)
    return () => clearTimeout(timeout)
  }, [query])

  useEffect(() => {
    setCurrentIndex(0)
  }, [debouncedQuery])

  useEffect(() => {
    const applyHighlight = (index: number): void => {
      const ranges = rangesRef.current
      if (!ranges.length) {
        CSS.highlights.delete(HIGHLIGHT_ALL)
        CSS.highlights.delete(HIGHLIGHT_CURRENT)
        return
      }
      CSS.highlights.set(HIGHLIGHT_ALL, new Highlight(...ranges))
      const current = ranges[index % ranges.length]
      CSS.highlights.set(HIGHLIGHT_CURRENT, new Highlight(current))
      current.startContainer.parentElement?.scrollIntoView({ block: 'center' })
    }

    const container = containerRef.current
    if (!container || !debouncedQuery) {
      rangesRef.current = []
      setMatchCount(0)
      CSS.highlights.delete(HIGHLIGHT_ALL)
      CSS.highlights.delete(HIGHLIGHT_CURRENT)
      return
    }

    const refreshMatches = (): void => {
      rangesRef.current = collectMatchRanges(container, debouncedQuery)
      setMatchCount(rangesRef.current.length)
      applyHighlight(currentIndex)
    }

    refreshMatches()

    // react-json-view mutates its own DOM when the user expands/collapses nodes -
    // re-run the search so matches stay in sync with what's actually visible.
    const observer = new MutationObserver(refreshMatches)
    observer.observe(container, { childList: true, subtree: true, characterData: true })

    return () => observer.disconnect()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [debouncedQuery])

  useEffect(() => {
    const ranges = rangesRef.current
    if (!ranges.length) return
    CSS.highlights.set(HIGHLIGHT_ALL, new Highlight(...ranges))
    const current = ranges[currentIndex % ranges.length]
    CSS.highlights.set(HIGHLIGHT_CURRENT, new Highlight(current))
    current.startContainer.parentElement?.scrollIntoView({ block: 'center' })
  }, [currentIndex])

  useEffect(() => {
    return () => {
      CSS.highlights.delete(HIGHLIGHT_ALL)
      CSS.highlights.delete(HIGHLIGHT_CURRENT)
    }
  }, [])

  const goToNext = (): void => setCurrentIndex((i) => (matchCount ? (i + 1) % matchCount : 0))
  const goToPrev = (): void =>
    setCurrentIndex((i) => (matchCount ? (i - 1 + matchCount) % matchCount : 0))

  return (
    <div
      onMouseEnter={() => (isHoveredRef.current = true)}
      onMouseLeave={() => (isHoveredRef.current = false)}
    >
      <div ref={containerRef}>
        <ReactJson {...props} />
      </div>
      <Group
        gap="xs"
        wrap="nowrap"
        p="xs"
        style={{
          position: 'sticky',
          bottom: 0,
          zIndex: 20,
          background: '#272822',
          borderTop: isOpen ? '1px solid #49483e' : 'none',
          overflow: 'hidden',
          maxHeight: isOpen ? 48 : 0,
          opacity: isOpen ? 1 : 0,
          transition: 'max-height 180ms ease, opacity 150ms ease, border-color 180ms ease'
        }}
      >
        <TextInput
          ref={inputRef}
          placeholder="Find in JSON..."
          leftSection={<IconSearch size={14} />}
          value={query}
          onChange={(e) => setQuery(e.currentTarget.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              e.preventDefault()
              if (e.shiftKey) goToPrev()
              else goToNext()
            } else if (e.key === 'Escape') {
              e.preventDefault()
              close()
            }
          }}
          size="xs"
          style={{ flex: 1 }}
          tabIndex={isOpen ? 0 : -1}
        />
        <Text size="xs" c="dimmed" style={{ whiteSpace: 'nowrap' }}>
          {matchCount ? `${(currentIndex % matchCount) + 1}/${matchCount}` : '0/0'}
        </Text>
        <ActionIcon size="sm" variant="subtle" disabled={!matchCount} onClick={goToPrev}>
          <IconChevronUp size={14} />
        </ActionIcon>
        <ActionIcon size="sm" variant="subtle" disabled={!matchCount} onClick={goToNext}>
          <IconChevronDown size={14} />
        </ActionIcon>
        <ActionIcon size="sm" variant="subtle" onClick={close}>
          <IconX size={14} />
        </ActionIcon>
      </Group>
    </div>
  )
}
