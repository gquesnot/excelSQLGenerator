from excel_class.excel_sql import ExcelSql
from excel_class.base_filter import BaseFilter

from value_class.complex_value import ComplexValue
from value_class.simple_value import SimpleValue
from value_class.equality_type import EqualityType

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