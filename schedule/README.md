```py
class Facts(Base):
    __tablename__ = "facts"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    author = Column(String, nullable=False)
    category = Column(String, nullable=False)
    last_used = Column(DateTime, nullable=False)
```