import Twin from '@/components/twin';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 to-gray-100 flex items-center justify-center p-4 sm:p-6">
      <div className="w-full max-w-4xl h-[700px]">
        <Twin />
      </div>
    </main>
  );
}