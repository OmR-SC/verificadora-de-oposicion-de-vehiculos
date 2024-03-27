
def sheet_writter(data,data_frame=None,cedula=None,row=None):
    
    if cedula == None:
        index = row-2
        if data[index][6] == "ACTIVO":
            data_frame.cell(row=row, column=4).value = data[index][6]
            data_frame.cell(row=row, column=5).value = "HALLAZGO"
        else:
            if data[index][6] == "Error":
                data_frame.cell(row=row, column=5).value = "ERROR"
            else:
                data_frame.cell(row=row, column=4).value = data[index][6]
                data_frame.cell(row=row, column=5).value = "REVISION"
                      
    else:
        max_rows = data_frame.max_row
        index = 0
        for row in range(2, max_rows + 1):
            placa = data_frame.cell(row=row, column=2).value
            cedula_cell = str(data_frame.cell(row=row, column=3).value)
            if placa == data[index][1] and cedula_cell == cedula:
                if data[index][6] == "ACTIVO":
                    data_frame.cell(row=row, column=4).value = data[index][6]
                    data_frame.cell(row=row, column=5).value = "HALLAZGO"
                else:
                    if data[index][6] == "Error":
                        data_frame.cell(row=row, column=5).value = "ERROR"
                
                    else:
                        data_frame.cell(row=row, column=4).value = data[index][6]
                        data_frame.cell(row=row, column=5).value = "REVISION"
                return True             
        return False
                