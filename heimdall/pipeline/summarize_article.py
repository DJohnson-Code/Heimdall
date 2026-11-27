from heimdall.schemas.schemas import NewsArticle, ArticleAnalysis, ProcessedArticle, SummaryInput
from heimdall.config.agent_model import model
from heimdall.config.summary_prompt import SUMMARIZER_SYSTEM_PROMPT

structured_model_response = model.with_structured_output(ArticleAnalysis)
MAX_ARTICLE_CHARS = 30_000

def prepare_article_input(articles: list[NewsArticle]) -> list[SummaryInput]: 
    summary_input: list[SummaryInput] = []

    for article in articles:
        prepared_article = SummaryInput(
            title = article.title,
            article = article.article[:MAX_ARTICLE_CHARS],
            publisher = article.publisher,
            published_at = article.published_at
        )

        summary_input.append(prepared_article)

    return summary_input

def summarize_article(articles: list[NewsArticle]) -> list[ProcessedArticle]: 
    articles_processed: list[ProcessedArticle] = []

    # Build one SummaryInput per article, with article text capped
    prepared_articles = prepare_article_input(articles)
    

    for original, prepared in zip(articles, prepared_articles, strict=True):
        summary_response = structured_model_response.invoke([
            ("system", SUMMARIZER_SYSTEM_PROMPT),
            ("human", prepared.model_dump_json())
        ])
        
        articles_processed.append(
            ProcessedArticle(
                article_id=original.id,
                title=original.title,
                url=original.url,
                publisher=original.publisher,
                published_at=original.published_at,
                category=summary_response.category,
                summary=summary_response.summary,
                relevance_score=summary_response.relevance_score
            )
        )
    return articles_processed

    # Configure structured output using ArticleAnalysis
    # (already defined at module level as structured_model_response).

    # TODO: Configure bounded retries and concurrency limits.

    # TODO: Submit the inputs using batch() with return_exceptions=True.

    # TODO: Match each response to its original NewsArticle.

    # TODO: Log and skip articles that failed after retries.

    # TODO: Combine successful ArticleAnalysis and News

    # TODO: Log the number of successful and failed analyses.

    # TODO: Return the list of ProcessedArticle objects.
    pass
