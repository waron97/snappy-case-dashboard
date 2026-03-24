import { Metadata } from 'next';

type Props = {
    params: Promise<{ record: string; model: string }>;
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
    const { record, model } = await params;
    return {
        title: `${model} #${record}`,
    };
}

export default function Layout({ children }: { children: React.ReactNode }) {
    return children;
}
