from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import datetime

engine = create_engine('postgresql://postgres:postgres@localhost:5432/iremdb')
Session = sessionmaker() 
Session.configure(bind=engine)
session=Session()
Base=declarative_base()

class Library(Base): 

    __tablename__='library'
    BookID=Column(Integer,primary_key=True)
    BookName=Column(String,nullable=False)
    Yearofpublication=Column(Integer,nullable=False)
    AuthorName=Column(String,nullable=False)
    Category=Column(String,nullable=False)
    Addp=Column(String,nullable=False)
    Book=relationship("Log",back_populates="lib")

    def __init__(self,BookName,Yearofpublication,AuthorName,Category,Addp):
        self.BookName=BookName
        self.Yearofpublication=Yearofpublication
        self.AuthorName=AuthorName
        self.Category=Category
        self.Addp=Addp


    def addClass(self):
        session.add(self)
        session.commit()




class Log(Base):

    __tablename__='log'
    BookID_log=Column(Integer,primary_key=True)
    Date=Column(String,nullable=False)
    Library_id=Column(Integer,ForeignKey('library.BookID'))
    lib=relationship("Library",back_populates="Book")
    Info=Column(String)
    Name=Column(String)
    OldVersion=Column(String)
    NewVersion=Column(String)

    def __init__(self,Library_id,Info,Name,OldVersion,NewVersion):
        self.Library_id=Library_id
        self.Date=datetime.datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        self.Info=Info
        self.Name=Name
        self.OldVersion=OldVersion
        self.NewVersion=NewVersion
       


    def addClass(self):
        session.add(self)
        session.commit()
    
    
Base.metadata.create_all(engine)

