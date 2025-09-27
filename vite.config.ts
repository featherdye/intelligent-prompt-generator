import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true,
    allowedHosts: [
      'intelligent-prompt-generator-production.up.railway.app',
      'localhost',
      '127.0.0.1',
      '.railway.app'
    ],
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@chakra-ui/react', '@emotion/react', '@emotion/styled'],
          forms: ['react-hook-form', 'zustand'],
        },
      },
    },
  },
  preview: {
    port: 3000,
    host: true,
    allowedHosts: [
      'intelligent-prompt-generator-production.up.railway.app',
      'localhost',
      '127.0.0.1',
      '.railway.app'
    ],
  },
})