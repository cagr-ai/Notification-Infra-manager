import { useState } from 'react'
import { Button } from '@/components/ui/button'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex min-h-svh flex-col items-center justify-center gap-6 p-8">
      <div className="flex flex-col items-center gap-2 text-center">
        <h1 className="text-3xl font-semibold tracking-tight">
          Notification infrastructure
        </h1>
        <p className="text-muted-foreground max-w-md text-sm">
          Vite + React + Tailwind + shadcn/ui (web) and FastAPI + MongoDB (api) in
          a pnpm + Turborepo monorepo.
        </p>
      </div>
      <Button type="button" onClick={() => setCount((c) => c + 1)}>
        Count is {count}
      </Button>
    </div>
  )
}

export default App
