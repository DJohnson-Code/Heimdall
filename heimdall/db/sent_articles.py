from sqlalchemy.orm import Session


def previously_sent_articles(session: Session, urls: list[str]) -> set[str]:
    if not urls: 
        return set()
    
    pass 

