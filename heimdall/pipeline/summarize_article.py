from heimdall.schemas.schemas import NewsArticle, ArticleAnalysis, ProcessedArticle, SummaryInput
from heimdall.config.agent_model import model

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
    # articles_processed: list[ProcessedArticle] = []

    # Extract relevant fields and cap article text length
    # (done by prepare_article_input).

    # Construct a list of individual LLM inputs.

    # Configure structured output using ArticleAnalysis
    # (already defined at module level as structured_model_response).

    # Configure bounded retries and concurrency limits.

    # Submit the inputs using batch() with return_exceptions=True.

    # Match each response to its original NewsArticle.

    # Log and skip articles that failed after retries.

    # Combine successful ArticleAnalysis and NewsArticle
    # objects to construct ProcessedArticle objects.

    # Log the number of successful and failed analyses.

    # Return the list of ProcessedArticle objects.
    pass
