
function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Intelligent Prompt Generator
          </h1>
          <p className="text-lg text-gray-600">
            Generate optimized prompts with advanced AI techniques
          </p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto">
          {/* Left Panel - Configuration Form */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-6">
              Configure Your Prompt
            </h2>
            <div className="space-y-4">
              <p className="text-gray-600">Configuration form will go here...</p>
            </div>
          </div>

          {/* Right Panel - Generated Prompt Display */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-6">
              Generated Prompt
            </h2>
            <div className="bg-gray-50 rounded-lg p-4 min-h-[400px]">
              <p className="text-gray-500 italic">
                Your optimized prompt will appear here...
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App