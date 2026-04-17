'use client';

import { useEffect, useRef } from 'react';
import { search } from '@codemirror/search';
import { vscodeDark } from '@uiw/codemirror-theme-vscode';
import ReactCodeMirror, { EditorView } from '@uiw/react-codemirror';
import { Text } from '@mantine/core';

type Props = {
    content: string | null;
    height?: string;
};

export default function LogViewer({ content, height = '700px' }: Props) {
    const viewRef = useRef<EditorView | null>(null);

    useEffect(() => {
        const view = viewRef.current;
        if (!view || content == null) {
            return;
        }
        view.dispatch({
            changes: { from: 0, to: view.state.doc.length, insert: content },
            selection: { anchor: content.length },
            scrollIntoView: true,
        });
    }, [content]);

    if (content == null) {
        return (
            <Text c="dimmed" size="sm" p="sm">
                No log available yet.
            </Text>
        );
    }

    return (
        <ReactCodeMirror
            readOnly
            theme={vscodeDark}
            height={height}
            onCreateEditor={(view) => {
                viewRef.current = view;
                // Populate initial content imperatively
                view.dispatch({
                    changes: { from: 0, to: 0, insert: content },
                    selection: { anchor: content.length },
                    scrollIntoView: true,
                });
            }}
            extensions={[search({ top: false })]}
            basicSetup={{
                lineNumbers: true,
                foldGutter: false,
                highlightActiveLine: false,
                searchKeymap: true,
            }}
        />
    );
}
