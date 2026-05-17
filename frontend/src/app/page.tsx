import Link from "next/link";

const featuredCities = ["La Paz", "Santa Cruz", "Cochabamba", "Remoto"];

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-50">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4">
          <Link className="text-xl font-bold text-brand-900" href="/">
            Duvi&apos;s Job.bo
          </Link>
          <nav className="hidden items-center gap-6 text-sm font-medium text-slate-600 sm:flex">
            <a className="hover:text-brand-700" href="#vacantes">
              Vacantes
            </a>
            <a className="hover:text-brand-700" href="#empresas">
              Empresas
            </a>
          </nav>
        </div>
      </header>

      <section className="bg-white">
        <div className="mx-auto grid min-h-[calc(100vh-73px)] max-w-6xl items-center gap-12 px-5 py-12 lg:grid-cols-[1.05fr_0.95fr] lg:py-16">
          <div>
            <p className="mb-4 inline-flex rounded-full bg-brand-50 px-4 py-2 text-sm font-semibold text-brand-700">
              Plataforma laboral para Bolivia
            </p>
            <h1 className="max-w-3xl text-4xl font-bold leading-tight text-brand-900 sm:text-5xl lg:text-6xl">
              Duvi&apos;s Job.bo
            </h1>
            <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
              Encuentra oportunidades reales, postula sin friccion y conecta
              con empresas que estan contratando en Bolivia.
            </p>

            <form
              aria-label="Busqueda de empleo"
              className="mt-8 rounded-lg border border-slate-200 bg-white p-3 shadow-soft"
            >
              <div className="grid gap-3 md:grid-cols-[1fr_0.7fr_auto]">
                <label className="sr-only" htmlFor="role">
                  Puesto o palabra clave
                </label>
                <input
                  className="min-h-12 rounded-md border border-slate-200 px-4 text-slate-900 outline-none transition focus:border-brand-600 focus:ring-2 focus:ring-brand-100"
                  id="role"
                  placeholder="Puesto, empresa o palabra clave"
                  type="search"
                />
                <label className="sr-only" htmlFor="location">
                  Ciudad
                </label>
                <input
                  className="min-h-12 rounded-md border border-slate-200 px-4 text-slate-900 outline-none transition focus:border-brand-600 focus:ring-2 focus:ring-brand-100"
                  id="location"
                  placeholder="Ciudad o remoto"
                  type="search"
                />
                <button
                  className="min-h-12 rounded-md bg-brand-700 px-6 font-semibold text-white transition hover:bg-brand-900 focus:outline-none focus:ring-2 focus:ring-brand-100"
                  type="button"
                >
                  Buscar empleo
                </button>
              </div>
            </form>

            <div className="mt-6 flex flex-col gap-3 sm:flex-row">
              <a
                className="inline-flex min-h-12 items-center justify-center rounded-md bg-brand-700 px-6 font-semibold text-white transition hover:bg-brand-900"
                href="#vacantes"
              >
                Buscar empleo
              </a>
              <a
                className="inline-flex min-h-12 items-center justify-center rounded-md border border-brand-700 px-6 font-semibold text-brand-700 transition hover:bg-brand-50"
                href="#empresas"
              >
                Publicar vacante
              </a>
            </div>
          </div>

          <aside
            aria-label="Resumen de oportunidades"
            className="rounded-lg border border-slate-200 bg-slate-50 p-5 shadow-soft"
          >
            <div className="rounded-md bg-white p-5">
              <p className="text-sm font-semibold uppercase tracking-wide text-brand-700">
                Vacantes destacadas
              </p>
              <div className="mt-5 space-y-4">
                {[
                  ["Analista comercial", "Santa Cruz", "Tiempo completo"],
                  ["Desarrollador frontend", "Remoto", "Contrato"],
                  ["Asistente contable", "La Paz", "Tiempo completo"],
                ].map(([title, city, type]) => (
                  <article
                    className="rounded-md border border-slate-200 bg-white p-4"
                    key={title}
                  >
                    <h2 className="text-base font-semibold text-slate-950">
                      {title}
                    </h2>
                    <p className="mt-2 text-sm text-slate-600">
                      {city} · {type}
                    </p>
                  </article>
                ))}
              </div>
            </div>
          </aside>
        </div>
      </section>

      <section
        className="border-y border-slate-200 bg-brand-900 px-5 py-14 text-white"
        id="vacantes"
      >
        <div className="mx-auto max-w-6xl">
          <h2 className="max-w-3xl text-3xl font-bold">
            Vacantes verificadas, postulaciones simples y oportunidades
            laborales para Bolivia.
          </h2>
          <div className="mt-8 grid gap-4 md:grid-cols-3">
            {[
              "Procesos claros para candidatos",
              "Herramientas simples para empresas",
              "Base preparada para roles y moderacion",
            ].map((item) => (
              <div className="rounded-lg bg-white/10 p-5" key={item}>
                <p className="font-semibold">{item}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-white px-5 py-12" id="empresas">
        <div className="mx-auto max-w-6xl">
          <div className="flex flex-col justify-between gap-6 md:flex-row md:items-end">
            <div>
              <h2 className="text-2xl font-bold text-slate-950">
                Explora por ciudad
              </h2>
              <p className="mt-2 max-w-2xl text-slate-600">
                Una base inicial enfocada en las principales plazas laborales y
                preparada para crecer con nuevas categorias.
              </p>
            </div>
            <Link
              className="inline-flex min-h-12 items-center justify-center rounded-md bg-accent-500 px-6 font-semibold text-brand-900 transition hover:bg-accent-600"
              href="/"
            >
              Publicar vacante
            </Link>
          </div>
          <div className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
            {featuredCities.map((city) => (
              <div
                className="rounded-lg border border-slate-200 bg-slate-50 p-5 font-semibold text-slate-800"
                key={city}
              >
                {city}
              </div>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
