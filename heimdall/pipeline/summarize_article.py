from heimdall.schemas.schemas import NewsArticle, ArticleAnalysis, ProcessedArticle, SummaryInput
from heimdall.config.agent_model import summarizer_model
from heimdall.config.summary_prompt import SUMMARIZER_SYSTEM_PROMPT
from openai import APIConnectionError, RateLimitError, InternalServerError
from pydantic import ValidationError
from langchain_core.exceptions import OutputParserException

structured_model_response = (
    summarizer_model
    .with_structured_output(ArticleAnalysis)
    .with_retry(
        retry_if_exception_type=(
            APIConnectionError,
            RateLimitError,
            InternalServerError,
            ValidationError,
            OutputParserException,
        ),
        stop_after_attempt=3,
        wait_exponential_jitter=True,
        exponential_jitter_params={
            "initial": 2,
            "max": 10,
        },
    )
)

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
        # retries and exception handling 
        try: 
            summary_response = structured_model_response.invoke([
                ("system", SUMMARIZER_SYSTEM_PROMPT),
                ("human", prepared.model_dump_json())
            ])
        except (APIConnectionError, RateLimitError, InternalServerError) as e:
            # Transient provider issues
            print(f"LLM call failed for: {original.url}, {original.id}: {e}")
        except (ValidationError, OutputParserException) as e:
            # Model produced output that doesn't match ArticleAnalysis schema
            print(f"Schema mismatch for: {original.url}, {original.id} {e}")
        else: 
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

    print(f"[debug] Articles submitted: {len(articles)}")
    print(f"[debug] Articles processed: {len(articles_processed)}")
    print(f"[debug] Articles failed: {len(articles) - len(articles_processed)}")


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
