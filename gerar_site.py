"""Gera as páginas do site em português, inglês e espanhol.

O conteúdo de cada idioma fica neste arquivo; o modelo da página é um só.
Para atualizar o site, edite o conteúdo abaixo e rode:

    python gerar_site.py
"""
from pathlib import Path

RAIZ = Path(__file__).parent
REVISAO = {"pt": "26/10/2026", "en": "26 Oct 2026", "es": "26/10/2026"}

IDIOMAS = {
    "pt": {"pasta": "", "html_lang": "pt-BR", "nome": "Português"},
    "en": {"pasta": "en/", "html_lang": "en", "nome": "English"},
    "es": {"pasta": "es/", "html_lang": "es", "nome": "Español"},
}

PAGINAS = ["index", "documentacao", "refugio", "apoio-sao-paulo", "aprender-portugues", "sobre"]

TEXTOS = {
    "pt": {
        "marca": "Primeiros Passos no Brasil",
        "pular": "Pular para o conteúdo",
        "menu": "Menu principal",
        "idioma": "Idioma",
        "nav": {
            "index": "Início",
            "documentacao": "Documentação",
            "refugio": "Refúgio",
            "apoio-sao-paulo": "Apoio em São Paulo",
            "aprender-portugues": "Aprender português",
            "sobre": "Sobre",
        },
        "rodape": "Projeto de extensão universitária de Igor Martins de Melo, Ciências da Computação, FAM.",
        "revisado": "Conteúdo revisado em {data}.",
        "saiba": "Saiba mais sobre o projeto",
        "aviso_traducao": "",
        "campos": {
            "tipo": "Tipo", "quem": "Quem oferece", "para": "Para quem", "abrangencia": "Abrangência",
            "custo": "Custo", "formato": "Formato", "idiomas": "Idiomas", "conferido": "Conferido em",
        },
    },
    "en": {
        "marca": "First Steps in Brazil",
        "pular": "Skip to content",
        "menu": "Main menu",
        "idioma": "Language",
        "nav": {
            "index": "Home",
            "documentacao": "Documents",
            "refugio": "Refuge",
            "apoio-sao-paulo": "Support in São Paulo",
            "aprender-portugues": "Learn Portuguese",
            "sobre": "About",
        },
        "rodape": "University extension project by Igor Martins de Melo, Computer Science, FAM.",
        "revisado": "Content reviewed on {data}.",
        "saiba": "Learn more about the project",
        "aviso_traducao": "This English version has not yet been reviewed by a native speaker. Most official pages linked here are in Portuguese.",
        "campos": {
            "tipo": "Type", "quem": "Offered by", "para": "For", "abrangencia": "Coverage",
            "custo": "Cost", "formato": "Format", "idiomas": "Languages", "conferido": "Checked on",
        },
    },
    "es": {
        "marca": "Primeros Pasos en Brasil",
        "pular": "Saltar al contenido",
        "menu": "Menú principal",
        "idioma": "Idioma",
        "nav": {
            "index": "Inicio",
            "documentacao": "Documentación",
            "refugio": "Refugio",
            "apoio-sao-paulo": "Apoyo en São Paulo",
            "aprender-portugues": "Aprender portugués",
            "sobre": "Acerca de",
        },
        "rodape": "Proyecto de extensión universitaria de Igor Martins de Melo, Ciencias de la Computación, FAM.",
        "revisado": "Contenido revisado el {data}.",
        "saiba": "Más información sobre el proyecto",
        "aviso_traducao": "Esta versión en español todavía no fue revisada por un hablante nativo. La mayoría de las páginas oficiales enlazadas están en portugués.",
        "campos": {
            "tipo": "Tipo", "quem": "Quién lo ofrece", "para": "Para quién", "abrangencia": "Alcance",
            "custo": "Costo", "formato": "Formato", "idiomas": "Idiomas", "conferido": "Verificado el",
        },
    },
}

# Datas de conferência dos links, no formato de cada idioma.
D26 = {"pt": "26/10/2026", "en": "26 Oct 2026", "es": "26/10/2026"}
D05 = {"pt": "05/10/2026", "en": "5 Oct 2026", "es": "05/10/2026"}

URL = {
    "crai": "https://prefeitura.sp.gov.br/web/imigrantes_e_trabalho_decente/w/crai/186981",
    "gov_refugio": "https://www.gov.br/pt-br/temas/refugio",
    "mj_refugio": "https://www.gov.br/mj/pt-br/assuntos/seus-direitos/refugio",
    "acnur": "https://help.unhcr.org/brazil/",
    "missao_paz": "https://missaonspaz.org/quem-somos/",
    "portas_abertas": "https://prefeitura.sp.gov.br/web/imigrantes_e_trabalho_decente/w/programas_e_projetos/portas_abertas/259310",
    "mapeamento": "https://imigrantesmapeamento.prefeitura.sp.gov.br/",
    "caderno_basico": "https://acervodigital.sme.prefeitura.sp.gov.br/wp-content/uploads/2021/08/caderno_basico_web.pdf",
    "caderno_intermediario": "https://acervodigital.sme.prefeitura.sp.gov.br/wp-content/uploads/2021/08/caderno_intermediario_web.pdf",
    "caderno_avancado": "https://acervodigital.sme.prefeitura.sp.gov.br/wp-content/uploads/2021/08/caderno_avancado_web.pdf",
    "duolingo_en": "https://www.duolingo.com/course/pt/en/Learn-Portuguese",
    "duolingo_es": "https://www.duolingo.com/course/pt/es/Aprender-portugu%C3%A9s",
}


def recurso(lang, titulo, descricao, campos, links):
    """Cartão de um serviço ou material: campos é uma lista de (chave, valor) e links de (texto, url)."""
    rotulos = TEXTOS[lang]["campos"]
    itens = "\n".join(f"        <dt>{rotulos[k]}</dt><dd>{v}</dd>" for k, v in campos)
    ligacoes = "\n".join(f'      <p><a class="link-oficial" href="{u}">{t}</a></p>' for t, u in links)
    return f"""
    <article class="recurso">
      <h3>{titulo}</h3>
      <p>{descricao}</p>
      <dl>
{itens}
      </dl>
{ligacoes}
    </article>"""


def emergencia(lang):
    nomes = {
        "pt": ("SAMU: emergência de saúde", "Polícia Militar", "Corpo de Bombeiros", "Disque Direitos Humanos"),
        "en": ("SAMU: medical emergency", "Military Police", "Fire Department", "Human Rights hotline"),
        "es": ("SAMU: emergencia de salud", "Policía Militar", "Bomberos", "Línea de Derechos Humanos"),
    }[lang]
    numeros = ("192", "190", "193", "100")
    itens = "\n".join(f"      <li><strong>{n}</strong> {t}</li>" for n, t in zip(numeros, nomes))
    return f'    <ul class="emergencia">\n{itens}\n    </ul>'


def aviso(texto):
    return f'\n    <div class="aviso">\n      <p>{texto}</p>\n    </div>'


# ---------------------------------------------------------------- conteúdo

def conteudo_index(lang):
    t = {
        "pt": dict(
            titulo="Orientação para quem chegou ao Brasil",
            intro="Encontre fontes oficiais sobre documentação e refúgio, serviços que podem orientar você e lugares para aprender português. Escolha o assunto de que precisa.",
            assuntos=[
                ("documentacao", "Documentação", "Onde buscar informação sobre documentos para viver e trabalhar no Brasil."),
                ("refugio", "Refúgio", "Informações para pessoas refugiadas e para quem quer pedir refúgio."),
                ("apoio-sao-paulo", "Apoio em São Paulo", "Serviços que atendem imigrantes na cidade de São Paulo."),
                ("aprender-portugues", "Aprender português", "Cursos gratuitos presenciais em São Paulo e materiais pela internet."),
            ],
            aviso="<strong>Importante:</strong> este site não é um serviço oficial. Os procedimentos variam conforme a situação de cada pessoa. Confirme sempre os requisitos no serviço responsável.",
            emerg_titulo="Em caso de emergência",
            emerg_texto="Os números abaixo são gratuitos e funcionam em todo o Brasil, mesmo sem documentos.",
        ),
        "en": dict(
            titulo="Guidance for people who have just arrived in Brazil",
            intro="Find official sources about documents and refuge, services that can guide you and places to learn Portuguese. Choose the topic you need.",
            assuntos=[
                ("documentacao", "Documents", "Where to find information about documents to live and work in Brazil."),
                ("refugio", "Refuge", "Information for refugees and for people who want to apply for refuge."),
                ("apoio-sao-paulo", "Support in São Paulo", "Services that assist immigrants in the city of São Paulo."),
                ("aprender-portugues", "Learn Portuguese", "Free in-person courses in São Paulo and online materials."),
            ],
            aviso="<strong>Important:</strong> this is not an official service. Procedures vary according to each person's situation. Always confirm the requirements with the responsible service.",
            emerg_titulo="In an emergency",
            emerg_texto="These numbers are free and work anywhere in Brazil, even without documents.",
        ),
        "es": dict(
            titulo="Orientación para quien llegó a Brasil",
            intro="Encuentra fuentes oficiales sobre documentación y refugio, servicios que pueden orientarte y lugares para aprender portugués. Elige el tema que necesitas.",
            assuntos=[
                ("documentacao", "Documentación", "Dónde buscar información sobre documentos para vivir y trabajar en Brasil."),
                ("refugio", "Refugio", "Información para personas refugiadas y para quien quiere solicitar refugio."),
                ("apoio-sao-paulo", "Apoyo en São Paulo", "Servicios que atienden a inmigrantes en la ciudad de São Paulo."),
                ("aprender-portugues", "Aprender portugués", "Cursos gratuitos presenciales en São Paulo y materiales en internet."),
            ],
            aviso="<strong>Importante:</strong> este sitio no es un servicio oficial. Los trámites varían según la situación de cada persona. Confirma siempre los requisitos en el servicio responsable.",
            emerg_titulo="En caso de emergencia",
            emerg_texto="Estos números son gratuitos y funcionan en todo Brasil, incluso sin documentos.",
        ),
    }[lang]
    assuntos = "\n".join(
        f'      <li>\n        <a href="{p}.html">\n          <strong>{n}</strong>\n          {d}\n        </a>\n      </li>'
        for p, n, d in t["assuntos"]
    )
    return t["titulo"], f"""
    <h1>{t["titulo"]}</h1>
    <p class="introducao">{t["intro"]}</p>

    <ul class="assuntos">
{assuntos}
    </ul>
{aviso(t["aviso"])}

    <h2>{t["emerg_titulo"]}</h2>
    <p>{t["emerg_texto"]}</p>
{emergencia(lang)}"""


def conteudo_documentacao(lang):
    if lang == "pt":
        titulo = "Documentação"
        corpo = f"""
    <h1>Documentação</h1>
    <p class="introducao">Migração e refúgio são situações diferentes, com procedimentos diferentes. Os documentos de que você precisa dependem da sua situação.</p>

    <h2>Antes de começar</h2>
    <ul>
      <li>Não existe uma lista de documentos que sirva para todas as pessoas.</li>
      <li>Busque orientação em um serviço oficial ou em uma instituição de apoio antes de iniciar um pedido.</li>
      <li>Desconfie de quem cobra para "garantir" documentos ou prazos.</li>
    </ul>

    <h2>Seus direitos</h2>
    <p>A Lei de Migração (Lei nº 13.445, de 2017) garante às pessoas migrantes acesso a serviços públicos de saúde, educação e assistência social, nas mesmas condições que as pessoas brasileiras.</p>

    <h2>Onde buscar orientação</h2>
{recurso(lang, "CRAI Oriana Jara", "Orientação sobre documentação, acesso a serviços e direitos, atendimento social e encaminhamentos.",
         [("quem", "Prefeitura de São Paulo"), ("abrangencia", "Cidade de São Paulo"), ("idiomas", "Atendimento multilíngue"), ("conferido", D26[lang])],
         [("Página oficial do CRAI, com endereço e horários atuais", URL["crai"])])}
{recurso(lang, "Refúgio no Governo Federal", "Informações oficiais sobre o pedido de refúgio e os serviços relacionados.",
         [("quem", "Governo Federal"), ("abrangencia", "Todo o Brasil"), ("idiomas", "Português"), ("conferido", D26[lang])],
         [("Página de serviços de refúgio no gov.br", URL["gov_refugio"])])}
{aviso("Este site não analisa a sua situação migratória e não substitui a orientação de um serviço oficial. Não envie documentos ou dados pessoais por este site.")}"""
    elif lang == "en":
        titulo = "Documents"
        corpo = f"""
    <h1>Documents</h1>
    <p class="introducao">Migration and refuge are different situations, with different procedures. The documents you need depend on your situation.</p>

    <h2>Before you start</h2>
    <ul>
      <li>There is no single list of documents that applies to everyone.</li>
      <li>Get guidance from an official service or a support organization before starting an application.</li>
      <li>Be wary of anyone who charges money to "guarantee" documents or deadlines.</li>
    </ul>

    <h2>Your rights</h2>
    <p>Brazil's Migration Law (Law No. 13,445 of 2017) guarantees migrants access to public health, education and social assistance services, under the same conditions as Brazilians.</p>

    <h2>Where to get guidance</h2>
{recurso(lang, "CRAI Oriana Jara", "Guidance on documents, access to services and rights, social assistance and referrals.",
         [("quem", "São Paulo City Hall"), ("abrangencia", "City of São Paulo"), ("idiomas", "Multilingual service"), ("conferido", D26[lang])],
         [("Official CRAI page with current address and hours (in Portuguese)", URL["crai"])])}
{recurso(lang, "Refuge on the Federal Government portal", "Official information about applying for refuge and related services.",
         [("quem", "Federal Government"), ("abrangencia", "All of Brazil"), ("idiomas", "Portuguese"), ("conferido", D26[lang])],
         [("Refuge services on gov.br (in Portuguese)", URL["gov_refugio"])])}
{aviso("This site does not assess your immigration status and does not replace guidance from an official service. Do not send documents or personal data through this site.")}"""
    else:
        titulo = "Documentación"
        corpo = f"""
    <h1>Documentación</h1>
    <p class="introducao">Migración y refugio son situaciones diferentes, con trámites diferentes. Los documentos que necesitas dependen de tu situación.</p>

    <h2>Antes de empezar</h2>
    <ul>
      <li>No existe una lista de documentos que sirva para todas las personas.</li>
      <li>Busca orientación en un servicio oficial o en una institución de apoyo antes de iniciar una solicitud.</li>
      <li>Desconfía de quien cobra para "garantizar" documentos o plazos.</li>
    </ul>

    <h2>Tus derechos</h2>
    <p>La Ley de Migración de Brasil (Ley nº 13.445, de 2017) garantiza a las personas migrantes el acceso a los servicios públicos de salud, educación y asistencia social, en las mismas condiciones que las personas brasileñas.</p>

    <h2>Dónde buscar orientación</h2>
{recurso(lang, "CRAI Oriana Jara", "Orientación sobre documentación, acceso a servicios y derechos, atención social y derivaciones.",
         [("quem", "Municipalidad de São Paulo"), ("abrangencia", "Ciudad de São Paulo"), ("idiomas", "Atención multilingüe"), ("conferido", D26[lang])],
         [("Página oficial del CRAI, con dirección y horarios actuales (en portugués)", URL["crai"])])}
{recurso(lang, "Refugio en el Gobierno Federal", "Información oficial sobre la solicitud de refugio y los servicios relacionados.",
         [("quem", "Gobierno Federal"), ("abrangencia", "Todo Brasil"), ("idiomas", "Portugués"), ("conferido", D26[lang])],
         [("Servicios de refugio en gov.br (en portugués)", URL["gov_refugio"])])}
{aviso("Este sitio no analiza tu situación migratoria y no sustituye la orientación de un servicio oficial. No envíes documentos ni datos personales por este sitio.")}"""
    return titulo, corpo


def conteudo_refugio(lang):
    if lang == "pt":
        titulo = "Refúgio"
        corpo = f"""
    <h1>Refúgio</h1>
    <p class="introducao">Se você deixou seu país por perseguição, guerra ou grave violação de direitos humanos, pode ter direito a pedir refúgio no Brasil.</p>

    <h2>O que saber</h2>
    <ul>
      <li>O pedido de refúgio é analisado pelo Governo Federal. Somente o órgão responsável decide se o pedido é aceito.</li>
      <li>Pedir refúgio é gratuito.</li>
      <li>Busque orientação antes de fazer o pedido. As instituições abaixo podem ajudar.</li>
    </ul>

    <h2>Fontes oficiais</h2>
{recurso(lang, "Refúgio no Ministério da Justiça", "Informações sobre o refúgio no Brasil e sobre o órgão que analisa os pedidos.",
         [("quem", "Ministério da Justiça e Segurança Pública"), ("abrangencia", "Todo o Brasil"), ("idiomas", "Português"), ("conferido", D26[lang])],
         [("Página de refúgio do Ministério da Justiça", URL["mj_refugio"])])}
{recurso(lang, "ACNUR Brasil: portal de informações", "Orientações para pessoas refugiadas, solicitantes de refúgio e apátridas, com caminhos para buscar apoio.",
         [("quem", "ACNUR, Agência da ONU para Refugiados (organismo internacional)"), ("abrangencia", "Todo o Brasil"), ("idiomas", "Vários idiomas"), ("conferido", D05[lang])],
         [("Portal do ACNUR para pessoas refugiadas no Brasil", URL["acnur"])])}
{recurso(lang, "Refúgio no Governo Federal", "Página do gov.br que reúne os serviços digitais relacionados ao refúgio.",
         [("quem", "Governo Federal"), ("abrangencia", "Todo o Brasil"), ("idiomas", "Português"), ("conferido", D26[lang])],
         [("Serviços de refúgio no gov.br", URL["gov_refugio"])])}
{aviso("Não conte sua história pessoal nem envie documentos por redes sociais ou por pessoas que você não conhece. Procure diretamente um serviço oficial ou uma instituição de apoio.")}"""
    elif lang == "en":
        titulo = "Refuge"
        corpo = f"""
    <h1>Refuge</h1>
    <p class="introducao">If you left your country because of persecution, war or serious human rights violations, you may have the right to apply for refuge in Brazil.</p>

    <h2>What to know</h2>
    <ul>
      <li>Refuge applications are assessed by the Federal Government. Only the responsible authority decides whether an application is accepted.</li>
      <li>Applying for refuge is free.</li>
      <li>Get guidance before applying. The organizations below can help.</li>
    </ul>

    <h2>Official sources</h2>
{recurso(lang, "Refuge at the Ministry of Justice", "Information about refuge in Brazil and the authority that assesses applications.",
         [("quem", "Ministry of Justice and Public Security"), ("abrangencia", "All of Brazil"), ("idiomas", "Portuguese"), ("conferido", D26[lang])],
         [("Ministry of Justice refuge page (in Portuguese)", URL["mj_refugio"])])}
{recurso(lang, "UNHCR Brazil: information portal", "Guidance for refugees, asylum seekers and stateless people, with ways to find support.",
         [("quem", "UNHCR, the UN Refugee Agency (international organization)"), ("abrangencia", "All of Brazil"), ("idiomas", "Several languages"), ("conferido", D05[lang])],
         [("UNHCR portal for refugees in Brazil", URL["acnur"])])}
{recurso(lang, "Refuge on the Federal Government portal", "The gov.br page that brings together the digital services related to refuge.",
         [("quem", "Federal Government"), ("abrangencia", "All of Brazil"), ("idiomas", "Portuguese"), ("conferido", D26[lang])],
         [("Refuge services on gov.br (in Portuguese)", URL["gov_refugio"])])}
{aviso("Do not share your personal story or send documents through social media or to people you do not know. Go directly to an official service or a support organization.")}"""
    else:
        titulo = "Refugio"
        corpo = f"""
    <h1>Refugio</h1>
    <p class="introducao">Si dejaste tu país por persecución, guerra o grave violación de derechos humanos, puedes tener derecho a solicitar refugio en Brasil.</p>

    <h2>Qué saber</h2>
    <ul>
      <li>La solicitud de refugio es analizada por el Gobierno Federal. Solo el órgano responsable decide si la solicitud es aceptada.</li>
      <li>Solicitar refugio es gratuito.</li>
      <li>Busca orientación antes de presentar la solicitud. Las instituciones de abajo pueden ayudar.</li>
    </ul>

    <h2>Fuentes oficiales</h2>
{recurso(lang, "Refugio en el Ministerio de Justicia", "Información sobre el refugio en Brasil y sobre el órgano que analiza las solicitudes.",
         [("quem", "Ministerio de Justicia y Seguridad Pública"), ("abrangencia", "Todo Brasil"), ("idiomas", "Portugués"), ("conferido", D26[lang])],
         [("Página de refugio del Ministerio de Justicia (en portugués)", URL["mj_refugio"])])}
{recurso(lang, "ACNUR Brasil: portal de información", "Orientaciones para personas refugiadas, solicitantes de refugio y apátridas, con caminos para buscar apoyo.",
         [("quem", "ACNUR, la Agencia de la ONU para los Refugiados (organismo internacional)"), ("abrangencia", "Todo Brasil"), ("idiomas", "Varios idiomas"), ("conferido", D05[lang])],
         [("Portal del ACNUR para personas refugiadas en Brasil", URL["acnur"])])}
{recurso(lang, "Refugio en el Gobierno Federal", "Página de gov.br que reúne los servicios digitales relacionados con el refugio.",
         [("quem", "Gobierno Federal"), ("abrangencia", "Todo Brasil"), ("idiomas", "Portugués"), ("conferido", D26[lang])],
         [("Servicios de refugio en gov.br (en portugués)", URL["gov_refugio"])])}
{aviso("No cuentes tu historia personal ni envíes documentos por redes sociales o a personas que no conoces. Acude directamente a un servicio oficial o a una institución de apoyo.")}"""
    return titulo, corpo


def conteudo_apoio(lang):
    if lang == "pt":
        titulo = "Apoio em São Paulo"
        corpo = f"""
    <h1>Apoio em São Paulo</h1>
    <p class="introducao">Serviços que atendem imigrantes e pessoas refugiadas na cidade de São Paulo. Endereços e horários mudam: consulte sempre a página oficial antes de ir.</p>
{recurso(lang, "CRAI Oriana Jara", "Centro de Referência e Atendimento para Imigrantes. Orienta sobre documentação, direitos e acesso a serviços, faz atendimento social e encaminhamentos.",
         [("tipo", "Serviço público municipal"), ("quem", "Prefeitura de São Paulo"), ("para", "Imigrantes e pessoas refugiadas"), ("idiomas", "Atendimento multilíngue"), ("conferido", D26[lang])],
         [("Atendimento do CRAI na página da Prefeitura", URL["crai"])])}
{recurso(lang, "Missão Paz", "Instituição filantrópica de acolhimento a imigrantes e refugiados. Inclui a Casa do Migrante e o Centro Pastoral e de Mediação dos Migrantes.",
         [("tipo", "Instituição do terceiro setor"), ("quem", "Missão Paz"), ("para", "Imigrantes e pessoas refugiadas"), ("idiomas", "Confirmar na página da instituição"), ("conferido", D05[lang])],
         [("Apresentação e canais da Missão Paz", URL["missao_paz"])])}
{recurso(lang, "ACNUR Brasil", "Agência da ONU para Refugiados. O portal ajuda a encontrar instituições de apoio em diferentes cidades, inclusive São Paulo.",
         [("tipo", "Organismo internacional"), ("quem", "ACNUR"), ("para", "Pessoas refugiadas, solicitantes de refúgio e apátridas"), ("idiomas", "Vários idiomas"), ("conferido", D05[lang])],
         [("Portal do ACNUR para pessoas refugiadas no Brasil", URL["acnur"])])}

    <h2>Saúde, escola e assistência social</h2>
    <p>Pessoas migrantes podem usar o SUS, matricular filhos na escola pública e procurar o CRAS do bairro para assistência social. Se não souber por onde começar, o CRAI pode orientar e encaminhar.</p>"""
    elif lang == "en":
        titulo = "Support in São Paulo"
        corpo = f"""
    <h1>Support in São Paulo</h1>
    <p class="introducao">Services that assist immigrants and refugees in the city of São Paulo. Addresses and opening hours change: always check the official page before you go.</p>
{recurso(lang, "CRAI Oriana Jara", "Reference and Service Center for Immigrants. Provides guidance on documents, rights and access to services, social assistance and referrals.",
         [("tipo", "Municipal public service"), ("quem", "São Paulo City Hall"), ("para", "Immigrants and refugees"), ("idiomas", "Multilingual service"), ("conferido", D26[lang])],
         [("CRAI services on the City Hall website (in Portuguese)", URL["crai"])])}
{recurso(lang, "Missão Paz", "A charitable organization that welcomes immigrants and refugees. It includes the Casa do Migrante shelter and a pastoral and mediation center for migrants.",
         [("tipo", "Non-profit organization"), ("quem", "Missão Paz"), ("para", "Immigrants and refugees"), ("idiomas", "Check on the organization's website"), ("conferido", D05[lang])],
         [("About Missão Paz and how to contact them (in Portuguese)", URL["missao_paz"])])}
{recurso(lang, "UNHCR Brazil", "The UN Refugee Agency. Its portal helps you find support organizations in different cities, including São Paulo.",
         [("tipo", "International organization"), ("quem", "UNHCR"), ("para", "Refugees, asylum seekers and stateless people"), ("idiomas", "Several languages"), ("conferido", D05[lang])],
         [("UNHCR portal for refugees in Brazil", URL["acnur"])])}

    <h2>Health, school and social assistance</h2>
    <p>Migrants can use SUS (the public health system), enroll their children in public school and go to the local CRAS (social assistance center). If you do not know where to start, CRAI can guide and refer you.</p>"""
    else:
        titulo = "Apoyo en São Paulo"
        corpo = f"""
    <h1>Apoyo en São Paulo</h1>
    <p class="introducao">Servicios que atienden a inmigrantes y personas refugiadas en la ciudad de São Paulo. Direcciones y horarios cambian: consulta siempre la página oficial antes de ir.</p>
{recurso(lang, "CRAI Oriana Jara", "Centro de Referencia y Atención para Inmigrantes. Orienta sobre documentación, derechos y acceso a servicios, ofrece atención social y derivaciones.",
         [("tipo", "Servicio público municipal"), ("quem", "Municipalidad de São Paulo"), ("para", "Inmigrantes y personas refugiadas"), ("idiomas", "Atención multilingüe"), ("conferido", D26[lang])],
         [("Atención del CRAI en la página de la Municipalidad (en portugués)", URL["crai"])])}
{recurso(lang, "Missão Paz", "Institución filantrópica de acogida a inmigrantes y refugiados. Incluye la Casa do Migrante y un centro pastoral y de mediación para migrantes.",
         [("tipo", "Institución del tercer sector"), ("quem", "Missão Paz"), ("para", "Inmigrantes y personas refugiadas"), ("idiomas", "Confirmar en la página de la institución"), ("conferido", D05[lang])],
         [("Presentación y canales de Missão Paz (en portugués)", URL["missao_paz"])])}
{recurso(lang, "ACNUR Brasil", "Agencia de la ONU para los Refugiados. Su portal ayuda a encontrar instituciones de apoyo en diferentes ciudades, incluida São Paulo.",
         [("tipo", "Organismo internacional"), ("quem", "ACNUR"), ("para", "Personas refugiadas, solicitantes de refugio y apátridas"), ("idiomas", "Varios idiomas"), ("conferido", D05[lang])],
         [("Portal del ACNUR para personas refugiadas en Brasil", URL["acnur"])])}

    <h2>Salud, escuela y asistencia social</h2>
    <p>Las personas migrantes pueden usar el SUS (sistema público de salud), matricular a sus hijos en la escuela pública y acudir al CRAS del barrio para asistencia social. Si no sabes por dónde empezar, el CRAI puede orientarte y derivarte.</p>"""
    return titulo, corpo


def conteudo_portugues(lang):
    if lang == "pt":
        titulo = "Aprender português"
        corpo = f"""
    <h1>Aprender português</h1>
    <p class="introducao">Falar português ajuda a buscar trabalho, usar serviços públicos e conhecer pessoas. Há opções gratuitas presenciais em São Paulo e materiais para estudar pela internet.</p>

    <h2>Presencial em São Paulo</h2>
{recurso(lang, "Portas Abertas: Português para Imigrantes", "Curso público e gratuito da Prefeitura, em escolas municipais participantes, nos níveis básico, intermediário e avançado. A matrícula não depende da condição migratória ou documental.",
         [("quem", "Prefeitura de São Paulo (Educação e Direitos Humanos)"), ("custo", "Gratuito"), ("formato", "Presencial, em escolas da rede municipal"), ("para", "Imigrantes adultos. Em 2023, a idade mínima era 18 anos: confirme a regra atual"), ("conferido", D26[lang])],
         [("Página oficial do Portas Abertas", URL["portas_abertas"])])}
    <p>Como se inscrever: vá direto à escola participante mais próxima. Em 2023, a Prefeitura pedia um documento de identificação (brasileiro ou do seu país) e um comprovante de residência; quem não tem comprovante pode preencher uma declaração de residência. Para saber quais escolas participam hoje, ligue <strong>156</strong> (Central de Atendimento da Prefeitura).</p>
{recurso(lang, "Missão Paz", "Além do acolhimento, a instituição oferece cursos de português para imigrantes e pessoas refugiadas. Vagas e horários variam.",
         [("tipo", "Instituição do terceiro setor"), ("formato", "Presencial"), ("custo", "Confirmar com a instituição"), ("conferido", D05[lang])],
         [("Canais de contato da Missão Paz", URL["missao_paz"])])}
{recurso(lang, "Mapeamento Colaborativo da Prefeitura", "Plataforma da Prefeitura que reúne coletivos, associações e organizações que atuam com imigrantes em São Paulo, entre eles grupos que oferecem cursos de português.",
         [("quem", "Prefeitura de São Paulo"), ("abrangencia", "Cidade de São Paulo"), ("conferido", D26[lang])],
         [("Abrir o Mapeamento Colaborativo", URL["mapeamento"])])}

    <h2>Pela internet, de graça</h2>
{recurso(lang, "Cadernos do Portas Abertas", "Apostilas oficiais usadas no curso da Prefeitura, em PDF. Servem para estudar sozinho ou acompanhar as aulas.",
         [("quem", "Prefeitura de São Paulo"), ("custo", "Gratuito"), ("formato", "PDF para baixar"), ("conferido", D26[lang])],
         [("Caderno básico (PDF)", URL["caderno_basico"]), ("Caderno intermediário (PDF)", URL["caderno_intermediario"]), ("Caderno avançado (PDF)", URL["caderno_avancado"])])}
{recurso(lang, "Duolingo", "Aplicativo com curso de português do Brasil para quem fala inglês ou espanhol. A versão básica é gratuita; há uma assinatura paga opcional.",
         [("tipo", "Aplicativo privado"), ("custo", "Versão básica gratuita"), ("formato", "Celular ou computador"), ("conferido", D26[lang])],
         [("Curso para quem fala inglês", URL["duolingo_en"]), ("Curso para quem fala espanhol", URL["duolingo_es"])])}

    <h2>Dicas para praticar</h2>
    <ul>
      <li>Aprenda primeiro frases do dia a dia: cumprimentar, pedir informação, falar seu nome e endereço.</li>
      <li>Escute rádio, música ou vídeos em português, mesmo sem entender tudo.</li>
      <li>Converse com vizinhos e colegas. Errar faz parte do aprendizado.</li>
    </ul>"""
    elif lang == "en":
        titulo = "Learn Portuguese"
        corpo = f"""
    <h1>Learn Portuguese</h1>
    <p class="introducao">Speaking Portuguese helps you find work, use public services and meet people. There are free in-person options in São Paulo and materials to study online.</p>

    <h2>In person in São Paulo</h2>
{recurso(lang, "Portas Abertas: Portuguese for Immigrants", "A free public course run by São Paulo City Hall in participating municipal schools, at basic, intermediate and advanced levels. Enrollment does not depend on your immigration or document status.",
         [("quem", "São Paulo City Hall (Education and Human Rights departments)"), ("custo", "Free"), ("formato", "In person, at municipal schools"), ("para", "Adult immigrants. In 2023 the minimum age was 18: check the current rule"), ("conferido", D26[lang])],
         [("Official Portas Abertas page (in Portuguese)", URL["portas_abertas"])])}
    <p>How to enroll: go directly to the nearest participating school. In 2023, City Hall asked for an identity document (Brazilian or from your country) and proof of address; if you do not have proof of address, you can fill in a residence declaration. To find out which schools take part today, call <strong>156</strong> (City Hall service line, in Portuguese).</p>
{recurso(lang, "Missão Paz", "Besides welcoming people, the organization offers Portuguese courses for immigrants and refugees. Places and schedules vary.",
         [("tipo", "Non-profit organization"), ("formato", "In person"), ("custo", "Check with the organization"), ("conferido", D05[lang])],
         [("Missão Paz contact channels (in Portuguese)", URL["missao_paz"])])}
{recurso(lang, "City Hall Collaborative Map", "A City Hall platform listing groups, associations and organizations that work with immigrants in São Paulo, including groups that offer Portuguese courses.",
         [("quem", "São Paulo City Hall"), ("abrangencia", "City of São Paulo"), ("conferido", D26[lang])],
         [("Open the Collaborative Map (in Portuguese)", URL["mapeamento"])])}

    <h2>Online, for free</h2>
{recurso(lang, "Portas Abertas workbooks", "The official workbooks used in the City Hall course, in PDF. Use them to study on your own or alongside classes.",
         [("quem", "São Paulo City Hall"), ("custo", "Free"), ("formato", "PDF download"), ("conferido", D26[lang])],
         [("Basic workbook (PDF)", URL["caderno_basico"]), ("Intermediate workbook (PDF)", URL["caderno_intermediario"]), ("Advanced workbook (PDF)", URL["caderno_avancado"])])}
{recurso(lang, "Duolingo", "An app with a Brazilian Portuguese course for English speakers. The basic version is free; an optional paid subscription is available.",
         [("tipo", "Private app"), ("custo", "Basic version free"), ("formato", "Phone or computer"), ("conferido", D26[lang])],
         [("Portuguese course for English speakers", URL["duolingo_en"])])}

    <h2>Tips for practicing</h2>
    <ul>
      <li>Start with everyday phrases: greeting people, asking for directions, saying your name and address.</li>
      <li>Listen to radio, music or videos in Portuguese, even if you do not understand everything.</li>
      <li>Talk to neighbors and coworkers. Making mistakes is part of learning.</li>
    </ul>"""
    else:
        titulo = "Aprender portugués"
        corpo = f"""
    <h1>Aprender portugués</h1>
    <p class="introducao">Hablar portugués ayuda a buscar trabajo, usar los servicios públicos y conocer personas. Hay opciones gratuitas presenciales en São Paulo y materiales para estudiar por internet.</p>

    <h2>Presencial en São Paulo</h2>
{recurso(lang, "Portas Abertas: Portugués para Inmigrantes", "Curso público y gratuito de la Municipalidad, en escuelas municipales participantes, en los niveles básico, intermedio y avanzado. La matrícula no depende de la situación migratoria ni documental.",
         [("quem", "Municipalidad de São Paulo (Educación y Derechos Humanos)"), ("custo", "Gratuito"), ("formato", "Presencial, en escuelas municipales"), ("para", "Inmigrantes adultos. En 2023 la edad mínima era 18 años: confirma la regla actual"), ("conferido", D26[lang])],
         [("Página oficial de Portas Abertas (en portugués)", URL["portas_abertas"])])}
    <p>Cómo inscribirse: ve directamente a la escuela participante más cercana. En 2023, la Municipalidad pedía un documento de identidad (brasileño o de tu país) y un comprobante de domicilio; si no tienes comprobante, puedes completar una declaración de residencia. Para saber qué escuelas participan hoy, llama al <strong>156</strong> (línea de atención de la Municipalidad, en portugués).</p>
{recurso(lang, "Missão Paz", "Además de la acogida, la institución ofrece cursos de portugués para inmigrantes y personas refugiadas. Las vacantes y horarios varían.",
         [("tipo", "Institución del tercer sector"), ("formato", "Presencial"), ("custo", "Confirmar con la institución"), ("conferido", D05[lang])],
         [("Canales de contacto de Missão Paz (en portugués)", URL["missao_paz"])])}
{recurso(lang, "Mapeo Colaborativo de la Municipalidad", "Plataforma de la Municipalidad que reúne colectivos, asociaciones y organizaciones que trabajan con inmigrantes en São Paulo, entre ellos grupos que ofrecen cursos de portugués.",
         [("quem", "Municipalidad de São Paulo"), ("abrangencia", "Ciudad de São Paulo"), ("conferido", D26[lang])],
         [("Abrir el Mapeo Colaborativo (en portugués)", URL["mapeamento"])])}

    <h2>Por internet, gratis</h2>
{recurso(lang, "Cuadernos de Portas Abertas", "Los cuadernos oficiales usados en el curso de la Municipalidad, en PDF. Sirven para estudiar por tu cuenta o acompañar las clases.",
         [("quem", "Municipalidad de São Paulo"), ("custo", "Gratuito"), ("formato", "PDF para descargar"), ("conferido", D26[lang])],
         [("Cuaderno básico (PDF)", URL["caderno_basico"]), ("Cuaderno intermedio (PDF)", URL["caderno_intermediario"]), ("Cuaderno avanzado (PDF)", URL["caderno_avancado"])])}
{recurso(lang, "Duolingo", "Aplicación con un curso de portugués de Brasil para hispanohablantes. La versión básica es gratuita; hay una suscripción de pago opcional.",
         [("tipo", "Aplicación privada"), ("custo", "Versión básica gratuita"), ("formato", "Celular o computadora"), ("conferido", D26[lang])],
         [("Curso de portugués para hispanohablantes", URL["duolingo_es"])])}

    <h2>Consejos para practicar</h2>
    <ul>
      <li>Empieza por frases del día a día: saludar, pedir información, decir tu nombre y tu dirección.</li>
      <li>Escucha radio, música o videos en portugués, aunque no entiendas todo.</li>
      <li>Conversa con vecinos y compañeros. Equivocarse es parte del aprendizaje.</li>
    </ul>"""
    return titulo, corpo


def conteudo_sobre(lang):
    t = {
        "pt": dict(
            titulo="Sobre o projeto",
            intro="Primeiros Passos no Brasil é um projeto de extensão universitária com finalidade educativa.",
            secoes=[
                ("Quem fez", "<p>Igor Martins de Melo, estudante de Ciências da Computação da FAM, como atividade extensionista da proposta Migrantes e Refugiados.</p>"),
                ("Objetivo", "<p>Ajudar pessoas recém-chegadas ao Brasil a encontrar fontes confiáveis, serviços de orientação e lugares para aprender português, em linguagem simples e com acesso fácil pelo celular.</p>"),
                ("O que este site não é", "<ul>\n      <li>Não é um serviço oficial e não tem parceria com as instituições citadas.</li>\n      <li>Não oferece orientação jurídica individual.</li>\n      <li>Não decide nem acelera pedidos de documentos ou de refúgio.</li>\n    </ul>"),
                ("Fontes e revisão", "<p>As informações apontam para páginas oficiais do Governo Federal, da Prefeitura de São Paulo, do ACNUR e da Missão Paz. Cada serviço mostra a data em que foi conferido. A abrangência local é a cidade de São Paulo.</p>"),
                ("Idiomas", "<p>O site está disponível em português, inglês e espanhol. As versões em inglês e espanhol ainda não foram revisadas por falantes nativos.</p>"),
                ("Privacidade", "<p>Este site não tem cadastro, formulário nem ferramentas de rastreamento. Ele não coleta nenhuma informação de quem o visita.</p>"),
            ],
        ),
        "en": dict(
            titulo="About the project",
            intro="First Steps in Brazil is a university extension project with an educational purpose.",
            secoes=[
                ("Who made it", "<p>Igor Martins de Melo, a Computer Science student at FAM, as an extension activity on the topic of Migrants and Refugees.</p>"),
                ("Goal", "<p>To help people who have just arrived in Brazil find reliable sources, guidance services and places to learn Portuguese, in plain language and easy to use on a phone.</p>"),
                ("What this site is not", "<ul>\n      <li>It is not an official service and has no partnership with the organizations mentioned.</li>\n      <li>It does not provide individual legal advice.</li>\n      <li>It does not decide on or speed up document or refuge applications.</li>\n    </ul>"),
                ("Sources and review", "<p>The information points to official pages of the Federal Government, São Paulo City Hall, UNHCR and Missão Paz. Each service shows the date it was checked. The local coverage is the city of São Paulo.</p>"),
                ("Languages", "<p>The site is available in Portuguese, English and Spanish. The English and Spanish versions have not yet been reviewed by native speakers.</p>"),
                ("Privacy", "<p>This site has no sign-up, forms or tracking tools. It does not collect any information about visitors.</p>"),
            ],
        ),
        "es": dict(
            titulo="Acerca del proyecto",
            intro="Primeros Pasos en Brasil es un proyecto de extensión universitaria con finalidad educativa.",
            secoes=[
                ("Quién lo hizo", "<p>Igor Martins de Melo, estudiante de Ciencias de la Computación de la FAM, como actividad de extensión sobre Migrantes y Refugiados.</p>"),
                ("Objetivo", "<p>Ayudar a las personas recién llegadas a Brasil a encontrar fuentes confiables, servicios de orientación y lugares para aprender portugués, en lenguaje sencillo y con fácil acceso desde el celular.</p>"),
                ("Lo que este sitio no es", "<ul>\n      <li>No es un servicio oficial y no tiene convenio con las instituciones mencionadas.</li>\n      <li>No ofrece asesoría jurídica individual.</li>\n      <li>No decide ni acelera solicitudes de documentos o de refugio.</li>\n    </ul>"),
                ("Fuentes y revisión", "<p>La información remite a páginas oficiales del Gobierno Federal, de la Municipalidad de São Paulo, del ACNUR y de Missão Paz. Cada servicio muestra la fecha en que fue verificado. El alcance local es la ciudad de São Paulo.</p>"),
                ("Idiomas", "<p>El sitio está disponible en portugués, inglés y español. Las versiones en inglés y español todavía no fueron revisadas por hablantes nativos.</p>"),
                ("Privacidad", "<p>Este sitio no tiene registro, formularios ni herramientas de rastreo. No recoge ninguna información de quien lo visita.</p>"),
            ],
        ),
    }[lang]
    secoes = "\n".join(f"\n    <h2>{h}</h2>\n    {c}" for h, c in t["secoes"])
    return t["titulo"], f"""
    <h1>{t["titulo"]}</h1>
    <p class="introducao">{t["intro"]}</p>
{secoes}"""


CONTEUDO = {
    "index": conteudo_index,
    "documentacao": conteudo_documentacao,
    "refugio": conteudo_refugio,
    "apoio-sao-paulo": conteudo_apoio,
    "aprender-portugues": conteudo_portugues,
    "sobre": conteudo_sobre,
}

DESCRICOES = {
    "pt": "Orientação para quem chegou ao Brasil: documentação, refúgio, apoio em São Paulo e onde aprender português.",
    "en": "Guidance for people who have just arrived in Brazil: documents, refuge, support in São Paulo and where to learn Portuguese.",
    "es": "Orientación para quien llegó a Brasil: documentación, refugio, apoyo en São Paulo y dónde aprender portugués.",
}


# ---------------------------------------------------------------- modelo

def montar(lang, pagina):
    t = TEXTOS[lang]
    prefixo = "../" if IDIOMAS[lang]["pasta"] else ""
    titulo, corpo = CONTEUDO[pagina](lang)
    titulo_aba = t["marca"] if pagina == "index" else f'{titulo} | {t["marca"]}'

    atual_pagina = ' aria-current="page"'
    atual_idioma = ' aria-current="true"'
    nav = "\n".join(
        f'          <li><a href="{p}.html"{atual_pagina if p == pagina else ""}>{t["nav"][p]}</a></li>'
        for p in PAGINAS
    )
    alternativas = "\n".join(
        f'  <link rel="alternate" hreflang="{IDIOMAS[l]["html_lang"]}" href="{prefixo}{IDIOMAS[l]["pasta"]}{pagina}.html">'
        for l in IDIOMAS
    )
    troca = "\n".join(
        f'          <li><a href="{prefixo}{IDIOMAS[l]["pasta"]}{pagina}.html" lang="{IDIOMAS[l]["html_lang"]}" hreflang="{IDIOMAS[l]["html_lang"]}"'
        f'{atual_idioma if l == lang else ""}>{IDIOMAS[l]["nome"]}</a></li>'
        for l in IDIOMAS
    )
    aviso_traducao = f'\n  <p class="aviso-traducao conteudo">{t["aviso_traducao"]}</p>' if t["aviso_traducao"] else ""
    saiba = "" if pagina == "sobre" else f' <a href="sobre.html">{t["saiba"]}</a>.'

    return f"""<!doctype html>
<html lang="{IDIOMAS[lang]["html_lang"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo_aba}</title>
  <meta name="description" content="{DESCRICOES[lang]}">
{alternativas}
  <link rel="stylesheet" href="{prefixo}estilo.css">
</head>
<body>
  <a class="pular" href="#principal">{t["pular"]}</a>
  <header class="topo">
    <div class="conteudo">
      <div class="linha-topo">
        <a class="marca" href="index.html">{t["marca"]}</a>
        <nav class="idiomas" aria-label="{t["idioma"]}">
          <ul>
{troca}
          </ul>
        </nav>
      </div>
      <nav class="menu" aria-label="{t["menu"]}">
        <ul>
{nav}
        </ul>
      </nav>
    </div>
  </header>{aviso_traducao}

  <main id="principal" class="conteudo">{corpo}
  </main>

  <footer class="rodape conteudo">
    <p>{t["rodape"]}</p>
    <p>{t["revisado"].format(data=REVISAO[lang])}{saiba}</p>
  </footer>
</body>
</html>
"""


def main():
    for lang, info in IDIOMAS.items():
        pasta = RAIZ / info["pasta"]
        pasta.mkdir(exist_ok=True)
        for pagina in PAGINAS:
            (pasta / f"{pagina}.html").write_text(montar(lang, pagina), encoding="utf-8")
    print(f"{len(IDIOMAS) * len(PAGINAS)} páginas geradas.")


if __name__ == "__main__":
    main()
