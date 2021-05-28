# Import any DAObject classes that you will need
from docassemble.base.util import Individual, Person, DAObject
# Import the SQLObject and some associated utility functions
from docassemble.base.sql import alchemy_url, upgrade_db, SQLObject, SQLObjectRelationship
# Import SQLAlchemy names
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import sys

# Only allow these names (DAObject classes) to be imported with a modules block
#__all__ = ['Bank', 'Customer', 'BankCustomer']
__all__ = ['Processo', 'Requerido', 'ProcessoRequerido']

# Create the base class for SQLAlchemy table definitions
Base = declarative_base()

# SQLAlchemy table definition for a Processo
class ProcessoModel(Base):
    __tablename__ = 'processo'
    id = Column(Integer, primary_key=True)
    routing = Column(String(250), unique=True)
    name = Column(String(250))

# SQLAlchemy table definition for a Requerido
class RequeridoModel(Base):
    __tablename__ = 'requerido'
    id = Column(Integer, primary_key=True)
    cpf = Column(String(250), unique=True)
    first_name = Column(String(250))
    last_name = Column(String(250))   
    address = Column(String(250))
    unit = Column(String(250))
    city = Column(String(250))
    state = Column(String(250))
    zip = Column(String(250))
        
    nacionality = Column(String(250))
    capacity = Column(String(250))
    legal_personal_representative = Column(String(250))
    marital_status = Column(String(250))
    city_of_birth = Column(String(250))
    birth_date = Column(String(250))
    profession = Column(String(250))
    identity_document = Column(String(250))
    fathers_name = Column(String(250))
    mothers_name = Column(String(250))
    phone_number = Column(String(250))
#    uses_whatsapp = Column(Boolean())

# SQLAlchemy table definition for keeping track of which Banks have which Customers
class ProcessoRequeridoModel(Base):
    __tablename__ = 'processo_requerido'
    id = Column(Integer, primary_key=True)
    processo_id = Column(Integer, ForeignKey('processo.id', ondelete='CASCADE'), nullable=False)
    requerido_id = Column(Integer, ForeignKey('requerido.id', ondelete='CASCADE'), nullable=False)

# Form the URL for connecting to the database based on the "demo db" directive in the Configuration
url = alchemy_url('olhosdamata db')

# Build the "engine" for connecting to the SQL server, using the URL for the database.
engine = create_engine(url)

# Create the tables
Base.metadata.create_all(engine)

# Get SQLAlchemy ready
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)()

# Perform any necessary database schema updates using alembic, if there is an alembic
# directory and alembic.ini file in the package.
upgrade_db(url, __file__, engine)

# Define Bank as both a DAObject and SQLObject
class Processo(Person, SQLObject):
    # This tells the SQLObject code what the SQLAlchemy model is
    _model = ProcessoModel
    # This tells the SQLObject code how to access the database
    _session = DBSession
    # This indicates that an object is not ready to be saved to SQL unless the "name" column is defined
    _required = ['name']
    # This indicates that the human-readable unique identifier for the table is the column "routing"
    _uid = 'routing'
    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
        # This runs necessary SQLObject initialization code for the instance
        self.sql_init()
    # The db_get function specifies how to get attributes from the DAObject for purposes of setting SQL column values
    def db_get(self, column):
        if column == 'name':
            return self.name.text
        elif column == 'routing':
            return self.routing
    # The db_set function specifies how to set attributes of the DAObject on the basis of non-null SQL column values
    def db_set(self, column, value):
        if column == 'name':
            self.name.text = value
        elif column == 'routing':
            self.routing = value
    # The db_null function specifies how to delete attributes of the DAObject when the SQL column value becomes null
    def db_null(self, column):
        if column == 'name':
            del self.name.text
        elif column == 'routing':
            del self.routing
    # This is an example of a method that uses SQLAlchemy to return True or False
    def has_requerido(self, requerido):
        if not (self.ready() and requerido.ready()):
            raise Exception("has_requerido: cannot retrieve data")
        # this opens a connection to the SQL database
        db_entry = self._session.query(ProcessoRequeridoModel).filter(ProcessoRequeridoModel.processo_id == self.id, ProcessoRequeridoModel.requerido_id == requerido.id).first()
        if db_entry is None:
            return False
        return True
    # This is an example of a method that uses SQLAlchemy to add a record to the BankCustomer SQL table
    # to indicate that a bank has a customer.  Note that it is designed to be idempotent; it will not add
    # a duplicate record.
    def add_requerido(self, requerido):
        if not self.has_requerido(requerido):
            db_entry = ProcessoRequeridoModel(processo_id=self.id, requerido_id=requerido.id)
            self._session.add(db_entry)
            self._session.commit()
    # This is an example of a method that uses SQLAlchemy to return a list of Customer objects.
    # It uses the by_id() class method to return a Customer object for the given id.
    def get_requerido(self):
        if not self.ready():
            raise Exception("get_requerido: cannot retrieve data")
        results = list()
        for db_entry in self._session.query(ProcessoRequeridoModel).filter(ProcessoRequeridoModel.processo_id == self.id).all():
            results.append(Requerido.by_id(db_entry.requerido_id))
        return results
    # This is an example of a method that uses SQLAlchemy to delete a bank-customer relationship
    def del_requerido(self, requerido):
        if not (self.ready() and requerido.ready()):
            raise Exception("del_requerido: cannot retrieve data")
        self._session.query(ProcessoRequeridoModel).filter(ProcessoRequeridoModel.processo_id == self.id, ProcessoRequeridoModel.requerido_id == requerido.id).delete()
        self._session.commit()

class Requerido(Individual, SQLObject):
    _model = RequeridoModel
    _session = DBSession
    _required = ['first_name']
    _uid = 'cpf'
    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
        self.sql_init()
    def db_get(self, column):
        if column == 'cpf':
            return self.cpf
        elif column == 'first_name':
            return self.name.first
        elif column == 'last_name':
            return self.name.last
        elif column == 'address':
            return self.address.address
        elif column == 'unit':
            return self.address.unit
        elif column == 'city':
            return self.address.city
        elif column == 'state':
            return self.address.state
        elif column == 'zip':
            return self.address.zip
  #Added fields:          
        elif column == 'nacionality':
            return self.address.nacionality
        elif column == 'capacity':
            return self.address.capacity  
        elif column == 'legal_personal_representative':
            return self.address.legal_personal_representative 
        elif column == 'marital_status':
            return self.address.marital_status          
        elif column == 'city_of_birth':
            return self.address.city_of_birth 
        elif column == 'birth_date':
            return self.address.birth_date
        elif column == 'profession':
            return self.address.profession  
        elif column == 'identity_document':
            return self.address.identity_document          
        elif column == 'fathers_name':
            return self.address.fathers_name      
        elif column == 'mothers_name':
            return self.address.mothers_name         
        elif column == 'phone_number':
            return self.address.phone_number         
#        elif column == 'uses_whatsapp':
#            return self.address.uses_whatsapp
          
    def db_set(self, column, value):
        if column == 'cpf':
            self.cpf = value
        elif column == 'first_name':
            self.name.first = value
        elif column == 'last_name':
            self.name.last = value
        elif column == 'address':
            self.address.address = value
        elif column == 'unit':
            self.address.unit = value
        elif column == 'city':
            self.address.city = value
        elif column == 'state':
            self.address.state = value
        elif column == 'zip':
            self.address.zip = value

        elif column == 'nacionality':
            self.address.nacionality = value
        elif column == 'capacity':
            self.address.capacity = value
        elif column == 'legal_personal_representative':
            self.address.legal_personal_representative = value
        elif column == 'marital_status':
            self.address.marital_status = value        
        elif column == 'city_of_birth':
            self.address.city_of_birth = value
        elif column == 'birth_date':
            self.address.birth_date = value
        elif column == 'profession':
            self.address.profession = value
        elif column == 'identity_document':
            self.address.identity_document = value     
        elif column == 'fathers_name':
            self.address.fathers_name = value    
        elif column == 'mothers_name':
            self.address.mothers_name = value      
        elif column == 'phone_number':
            self.address.phone_number = value    
#        elif column == 'uses_whatsapp':
#           self.address.uses_whatsapp = value         
            
    def db_null(self, column):
        if column == 'cpf':
            del self.cpf
        elif column == 'first_name':
            del self.name.first
        elif column == 'last_name':
            del self.name.last
        elif column == 'address':
            del self.address.address
        elif column == 'unit':
            del self.address.unit
        elif column == 'city':
            del self.address.city
        elif column == 'state':
            del self.address.state
        elif column == 'zip':
            del self.address.zip

        elif column == 'nacionality':
            del self.address.nacionality
        elif column == 'capacity':
            del self.address.capacity
        elif column == 'legal_personal_representative':
            del self.address.legal_personal_representative
        elif column == 'marital_status':
            del self.address.marital_status        
        elif column == 'city_of_birth':
            del self.address.city_of_birth
        elif column == 'birth_date':
            del self.address.birth_date
        elif column == 'profession':
            del self.address.profession
        elif column == 'identity_document':
            del self.address.identity_document     
        elif column == 'fathers_name':
            del self.address.fathers_name    
        elif column == 'mothers_name':
            del self.address.mothers_name      
        elif column == 'phone_number':
            del self.address.phone_number    
#        elif column == 'uses_whatsapp':
#            del self.address.uses_whatsapp            
            
            
class ProcessoRequerido(DAObject, SQLObjectRelationship):
    _model = ProcessoRequeridoModel
    _session = DBSession
    _parent = [Processo, 'processo', 'processo_id']
    _child = [Requerido, 'requerido', 'requerido_id']
    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
        self.rel_init(*pargs, **kwargs)
    def db_get(self, column):
        if column == 'processo_id':
            return self.processo.id
        elif column == 'requerido_id':
            return self.requerido.id
    def db_set(self, column, value):
        if column == 'processo_id':
            self.bank = Processo.by_id(value)
        elif column == 'requerido_id':
            self.customer = Requerido.by_id(value)
    # A db_find_existing method is defined here because the default db_find_existing() method for
    # the SQLObject class tries to find existing records based on a unique identifier column indicated
    # by the _uid attribute.  Since the unique identifier for a bank-customer relationship record is
    # not a single column, but rather the combination of bank ID and customer ID, there is no _uid
    # column for the default db_find_existing() method to use.  But we can write our own method for
    # how to locate an existing record based on Python object attributes (.bank.id and .customer.id).
    def db_find_existing(self):
        try:
            return self._session.query(ProcessoRequeridoModel).filter(ProcessoRequeridoModel.processo_id == self.processo.id, ProcessoRequeridoModel.requerido_id == self.requerido.id).first()
        except:
            return None
#Correção do data_exata para evitar erros de digitação do usuário
def teste_data():
    if data_exata == "sim":
        return(data_fato)
    else:
        return("de maneira permanente, sendo o fato constatado na data da fiscalização ocorrida em", data_fato)