// Parses the Symphony execution-tree HTML into a typed node tree. Pure, no
// React — uses the renderer's native DOMParser (no cheerio/jsdom needed or
// present in this repo).
//
// Two endpoints return execution-tree HTML in different wrappers, but both
// are handled by the same function: getRequestDetailHtml's full detail page
// (root wrapped in #executionTreeContainer, with one level of children
// already embedded) and getExecutionTreeNode's single-node fragment (a bare
// `<div class="execution-node">…</div><div class="children-container">…</div>`
// for one previously-collapsed node, now expanded one level deeper). In both
// cases the first `.execution-node` in the parsed document is the node to
// return, so no shape-specific branching is needed.

import type { SymphonyExecutionNode } from '@/lib/symphony-api'

/**
 * Collects the DIRECT execution-node children of one `.children-container`,
 * robust to the markup's incidental div/ul wrapping (the node-endpoint sample
 * wraps its <li>s in a stray bare <div> before the <ul>). Keying off the
 * nearest `.children-container` ancestor rather than a fixed selector depth
 * means this is correct regardless of how deep that incidental nesting goes.
 */
function directChildNodes(container: Element): Element[] {
  return Array.from(container.querySelectorAll('.execution-node')).filter(
    (el) => el.closest('.children-container') === container
  )
}

function parseColor(style: string | null): string | null {
  if (!style) return null
  const match = style.match(/color:\s*([^;]+)/i)
  return match ? match[1].trim() : null
}

function parseNode(el: Element): SymphonyExecutionNode {
  const id = el.getAttribute('data-id') ?? ''
  const nameEl = el.querySelector('.node-name')
  const name = nameEl?.getAttribute('title') || nameEl?.textContent?.trim() || id
  const icon = el.querySelector('i.material-icons')
  const status = icon?.getAttribute('title') ?? null
  const statusColor = parseColor(icon?.getAttribute('style') ?? null)
  const hasChildren = el.classList.contains('has-children')

  const container = el.nextElementSibling
  const children =
    container && container.classList.contains('children-container')
      ? directChildNodes(container).map(parseNode)
      : []

  return { id, name, status, statusColor, hasChildren, children }
}

/**
 * Parses either shape of execution-tree HTML into its root node. Returns null
 * if the HTML has no `.execution-node` at all (shouldn't happen for either
 * verified endpoint, but a request mid-flight or an API change should degrade
 * to "nothing to show" rather than throw).
 */
export function parseExecutionTree(html: string): SymphonyExecutionNode | null {
  const doc = new DOMParser().parseFromString(html, 'text/html')
  const root = doc.querySelector('.execution-node')
  return root ? parseNode(root) : null
}
