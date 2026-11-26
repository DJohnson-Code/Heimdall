from pydantic import BaseModel, ConfigDict, Field

class TopicConfig(BaseModel): 
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    rss_sources: list[str] = Field(default_factory=list)
    trusted_domains: list[str] = Field(default_factory=list)
    search_queries: list[str] = Field(default_factory=list)
    max_articles: int = Field(ge=1, le=10)
    freshness_days: int = Field(ge=1, le=30)

    model_config = ConfigDict(extra="forbid")


ai_topic = TopicConfig(
    name = "AI",
    description = ("Recent developments in artificial intelligence, including major model releases, "
    "AI infrastructure, agent systems, open-source models, AI tooling, research breakthroughs, "
    "safety/regulation updates, and practical impacts on software engineering."),
    rss_sources = [
        "https://openai.com/news/rss.xml",
        "https://huggingface.co/blog/feed.xml",
    ], 
    trusted_domains = [
        "openai.com",
        "anthropic.com",
        "deepmind.google",
        "huggingface.co",
        "ai.googleblog.com",
    ],
    search_queries = [
        "latest AI model releases",
        "AI agents developer tools news",
        "open source LLM releases",
        "AI infrastructure inference serving news",
        "AI regulation safety policy updates",
    ], 
    max_articles = 5, 
    freshness_days = 5, 
)

backend_topic = TopicConfig(
    name = "Backend Engineering / Developer Tools",
    description = ("Backend engineering and developer tooling updates, including APIs, databases, "
    "distributed systems, observability, queues, caching, reliability, platform engineering, "
    "deployment tooling, internal tools, and practical engineering posts from strong software teams."),
    rss_sources = [
        "https://github.blog/feed/",
        "https://blog.cloudflare.com/rss/",
        "https://netflixtechblog.com/feed",
        "https://stripe.com/blog/feed.rss",
        "https://engineering.fb.com/feed/",
        "https://engineering.atspotify.com/feed/",
        "https://dropbox.tech/feed",
        "https://tailscale.com/blog/index.xml",
        "https://slack.engineering/feed/",
    ],
    trusted_domains = [
        "github.blog",
        "cloudflare.com",
        "netflixtechblog.com",
        "stripe.com",
        "uber.com",
        "engineering.fb.com",
        "engineering.linkedin.com",
        "slack.engineering",
        "discord.com",
        "engineering.atspotify.com",
        "airbnb.tech",
        "dropbox.tech",
        "shopify.engineering",
        "tailscale.com",
        "fly.io",
        "supabase.com",
        "planetscale.com",
        "postgresql.org",
        "canva.dev",
    ],
    search_queries = [
        "backend engineering blog distributed systems",
        "API design developer tools news",
        "database scaling engineering blog",
        "observability platform engineering news",
        "PostgreSQL performance release news",
        "queue worker architecture engineering blog",
        "developer tools startup infrastructure news",
    ],
    max_articles = 5,
    freshness_days = 7,
)

tech_markets_ipo_topic = TopicConfig(
    name = "Tech Markets / IPOs",
    description = ("Technology IPO and market-signal news, including companies preparing to go public, "
    "S-1 filings, confidential IPO filings, major funding rounds, acquisitions, market-moving company events, "
    "earnings, AI and infrastructure valuation trends, and investor sentiment around software, cloud, "
    "semiconductor, and developer-tool companies."),
    rss_sources = [
        "https://www.sec.gov/news/pressreleases.rss",
        "https://techcrunch.com/category/startups/feed/",
        "https://techcrunch.com/category/venture/feed/",
    ],
    trusted_domains = [
        "sec.gov",
        "nasdaq.com",
        "nyse.com",
        "reuters.com",
        "apnews.com",
        "cnbc.com",
        "marketwatch.com",
        "bloomberg.com",
        "wsj.com",
        "ft.com",
        "finance.yahoo.com",
        "techcrunch.com",
        "theinformation.com",
        "crunchbase.com",
        "renaissancecapital.com",
        "axios.com",
        "sherwood.news",
        "pitchbook.com",
    ],
    search_queries = [
        "technology company IPO filing S-1",
        "software company files for IPO",
        "AI company IPO filing",
        "cloud software company IPO news",
        "semiconductor company IPO market news",
        "tech company confidential IPO filing",
        "major tech acquisition software cloud AI",
        "developer tools company funding acquisition IPO",
        "public tech company earnings AI cloud infrastructure",
    ],
    max_articles = 4,
    freshness_days = 7,
)

cybersecurity_topic = TopicConfig(
    name = "Cybersecurity / API Security",
    description = ("Cybersecurity news relevant to software engineers and backend systems, including API security, "
    "software supply-chain attacks, authentication vulnerabilities, cloud security, breached developer tools, "
    "critical CVEs, CISA and OWASP advisories, npm/PyPI/GitHub ecosystem risks, container security, "
    "and secure coding practices."),
    rss_sources = [
        "https://www.cisa.gov/cybersecurity-advisories/all.xml",
        "https://portswigger.net/daily-swig/rss",
        "https://www.bleepingcomputer.com/feed/",
        "https://krebsonsecurity.com/feed/",
        "https://feeds.feedburner.com/TheHackersNews",
        "https://snyk.io/blog/feed/",
    ],
    trusted_domains = [
        "cisa.gov",
        "nist.gov",
        "nvd.nist.gov",
        "owasp.org",
        "portswigger.net",
        "krebsonsecurity.com",
        "bleepingcomputer.com",
        "thehackernews.com",
        "darkreading.com",
        "github.blog",
        "cloudflare.com",
        "snyk.io",
        "socket.dev",
        "wiz.io",
        "security.googleblog.com",
        "msrc.microsoft.com",
        "redhat.com",
        "sonatype.com",
        "trailofbits.com",
        "semgrep.dev",
        "chainguard.dev",
    ],
    search_queries = [
        "API security vulnerability developer impact",
        "software supply chain attack npm PyPI GitHub",
        "authentication vulnerability OAuth JWT session security",
        "cloud security vulnerability developer tools",
        "critical CVE exploited in the wild backend systems",
        "CISA known exploited vulnerabilities software developers",
        "OWASP API security updates",
        "package registry supply chain attack npm PyPI",
        "GitHub security advisory developer tooling",
        "container Kubernetes vulnerability developer impact",
    ],
    max_articles = 5,
    freshness_days = 3,
)

general_tech_topic = TopicConfig(
    name = "General Tech / Tech Business",
    description = ("Broad technology industry news and business context, including major product launches, "
    "company strategy, regulation, platform shifts, consumer technology, enterprise software, "
    "startup activity, acquisitions, leadership changes, and high-level trends affecting the tech industry."),
    rss_sources = [
        "https://www.technologyreview.com/feed/",
        "https://feeds.arstechnica.com/arstechnica/technology-lab",
        "https://techcrunch.com/feed/",
        "https://www.theverge.com/rss/tech/index.xml",
        "https://www.wired.com/feed/rss",
        "https://news.ycombinator.com/rss",
    ],
    trusted_domains = [
        "reuters.com",
        "apnews.com",
        "technologyreview.com",
        "arstechnica.com",
        "theverge.com",
        "wired.com",
        "axios.com",
        "techcrunch.com",
        "spectrum.ieee.org",
        "cacm.acm.org",
        "news.ycombinator.com",
    ],
    search_queries = [
        "major technology industry news",
        "big tech product platform strategy news",
        "tech regulation platform policy news",
        "enterprise software industry news",
        "startup technology business news",
        "consumer tech product launch news",
        "technology acquisitions leadership changes",
        "open internet platform ecosystem news",
    ],
    max_articles = 5,
    freshness_days = 5,
)

DAILY_TOPICS: list[TopicConfig] = [
    ai_topic,
    backend_topic,
    tech_markets_ipo_topic,
    cybersecurity_topic,
    general_tech_topic,
]