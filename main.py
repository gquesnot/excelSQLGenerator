from excel_class.excel_sql import ExcelSql
from excel_class.base_filter import BaseFilter

from value_class.complex_value import ComplexValue
from value_class.simple_value import SimpleValue
from value_class.equality_type import EqualityType

if __name__ == '__main__':
    # init class and set xlsx fileName
    excelSql = ExcelSql('test.xlsx')

    # init and UPDATE SQL request on table leads from the sheet leads start at the row 2
    excelSql.initReqSql(sqlType="update", table='leads', fromSheetName='leads', offset=2)

    # add a set  `email_2` = {entity.B where leads.Q contain  or is contained by entity.C}
    excelSql.addFilter(BaseFilter(type="set", field='email_2', value=ComplexValue( from_='leads.Q=entity.C', value='entity.B', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="set", field='entite_id', value=ComplexValue( from_='leads.Q=entity.C', value='entity.A', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="set", field='step_id', value=ComplexValue(from_='leads.R=step.B', value='step.A', equality=EqualityType.CONTAIN)))
    excelSql.addFilter(BaseFilter(type="set", field='job_id', value=ComplexValue(from_='leads.M=job.B', value='job.A', equality=EqualityType.CONTAIN)))

    # add a where email = leads.A show this request if mail is not null
    excelSql.addFilter(BaseFilter(type="where", field='email', value=SimpleValue(value='leads.A'), required=True))
    excelSql.addFilter(BaseFilter(type="where", field='nom', value=SimpleValue(value='leads.B')))
    excelSql.addFilter(BaseFilter(type="where", field='date_creation', value=SimpleValue(value='leads.L')))

    # get your requests like
    # update leads set `email_2` = 'mail@entite.com4', `entite_id` = 9, `step_id` = 4, `job_id` = 4 where `email` = 'mail@mail.com' and `nom` = 'nom' and `date_creation` = '2021-10-08 08:53:41';
    excelSql.generateSQL()