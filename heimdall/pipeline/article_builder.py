from heimdall.schemas.schemas import ArticleCandidate, FetchedArticle, NewsArticle


def article_builder(
    candidates: list[ArticleCandidate],
    article_cache: dict[str, FetchedArticle],
) -> list[NewsArticle]:
    
    articles: list[NewsArticle] = []



    for candidate in candidates: 
        fetched = article_cache.get(str(candidate.url))

        if fetched is None:
            continue

        news_article = NewsArticle(
            article=fetched.article, 
            title=candidate.title, 
            url=fetched.source, 
            publisher=candidate.publisher, 
            published_at=candidate.published_at,
        )

        articles.append(news_article)

    return articles 