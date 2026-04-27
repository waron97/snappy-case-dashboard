import bundleAnalyzer from '@next/bundle-analyzer';

const withBundleAnalyzer = bundleAnalyzer({
    enabled: process.env.ANALYZE === 'true',
});

export default withBundleAnalyzer({
    reactStrictMode: false,
    output: 'standalone',
    experimental: {
        serverActions: {
            allowedOrigins: ['snappy.aronwinkler.com', 'bbtucg.instatunnel.my'],
        },
    },
    env: {
        ODOO_URL: process.env.ODOO_URL,
        ...(process.env.PORT && { PORT: process.env.PORT }),
    },
});
