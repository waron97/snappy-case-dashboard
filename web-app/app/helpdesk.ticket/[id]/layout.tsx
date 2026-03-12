import { Metadata } from 'next';

type Props = {
  params: Promise<{ id: string }>;
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  return {
    title: `Case #${id}`,
  };
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return children;
}
