from ExcelClass.ExcelSql import ExcelSql
from ExcelClass.BaseFilter import BaseFilter

from valueClass.ComplexValue import ComplexValue
from valueClass.SimpleValue import SimpleValue
from valueClass.equality_type import EqualityType

if __name__ == '__main__':
    excelSql = ExcelSql('test.xlsx')
    excelSql.initReqSql(sqlType="update", table='leads', fromSheetName='leads', offset=1)
    excelSql.addFilter(BaseFilter(type="set", field='email_2', value=ComplexValue( from_='leads.Q=entity.C', value='entity.B', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="set", field='entite_id', value=ComplexValue( from_='leads.Q=entity.C', value='entity.A', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="set", field='step_id', value=ComplexValue(from_='leads.R=step.B', value='step.A', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="set", field='job_id', value=ComplexValue(from_='leads.M=job.B', value='job.A', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="where", field='email', value=SimpleValue(value='leads.A'), required=True))
    excelSql.addFilter(BaseFilter(type="where", field='nom', value=SimpleValue(value='leads.B')))
    excelSql.addFilter(BaseFilter(type="where", field='date_creation', value=SimpleValue(value='leads.L')))
    excelSql.generateSQL()