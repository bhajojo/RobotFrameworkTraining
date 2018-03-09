from xlrd import open_workbook, cellname, xldate_as_tuple, \
    XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_TEXT, XL_CELL_BOOLEAN, \
    XL_CELL_ERROR, XL_CELL_BLANK, XL_CELL_EMPTY, error_text_from_code


def get_row_values(self, sheetname, row, includeEmptyCells=True):
    """
    Returns the specific row values of the sheet name specified.

    Arguments:
            |  Sheet Name (string)                 | The selected sheet that the row values will be returned from.                                                               |
            |  Row (int)                           | The row integer value that will be used to select the row from which the values will be returned.                           |
            |  Include Empty Cells (default=True)  | The empty cells will be included by default. To deactivate and only return cells with values, pass 'False' in the variable. |
    Example:

    | *Keywords*           |  *Parameters*                                          |
    | Open Excel           |  C:\\Python27\\ExcelRobotTest\\ExcelRobotTest.xls  |   |
    | Get Row Values       |  TestSheet1                                        | 0 |

    """
    my_sheet_index = self.sheetNames.index(sheetname)
    sheet = self.wb.sheet_by_index(my_sheet_index)
    data = {}
    for col_index in range(sheet.ncols):
        cell = cellname(int(row), col_index)
        value = sheet.cell(int(row), col_index).value
        data[cell] = value
    if includeEmptyCells is True:
        sortedData = natsort.natsorted(data.items(), key=itemgetter(0))
        return sortedData
    else:
        data = dict([(k, v) for (k, v) in data.items() if v])
        OrderedData = natsort.natsorted(data.items(), key=itemgetter(0))
        return OrderedData

def cellname(rowx, colx):
    """Utility function: ``(5, 7)`` => ``'H6'``"""
    return "%s%d" % (colname(colx), rowx+1)