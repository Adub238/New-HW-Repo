Sub StockSummary():

    Dim lastRow As Long
    Dim currStock As String
    Dim openPrice As Double
    Dim closePrice As Double
    Dim totalSales As Double
    Dim yearlyChange As Double
    Dim percentChange As Single
    Dim summaryStock As Integer
    
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "Percent Change"
    Range("L1").Value = "Total Sales"
    Range("I1:L1").Font.Bold = True
    
     
    summaryStock = 2
    totalSales = 0
    currStock = Cells(2, 1).Value
    openPrice = Cells(2, 3).Value
    
    lastRow = Cells(Rows.Count, "A").End(xlUp).Row
    
    For I = 2 To (lastRow)
        totalSales = totalSales + Cells(I, 7).Value
        If Cells(I + 1, 1) <> Cells(I, 1) Then
            closePrice = Cells(I, 6).Value
            yearlyChange = closePrice - openPrice
            If openPrice = 0 Then
                percentChange = 0
            Else
                percentChange = yearlyChange / openPrice
            End If
            Cells(summaryStock, 9).Value = currStock
            Cells(summaryStock, 10).Value = Round(yearlyChange, 2)
            Cells(summaryStock, 11).Value = (Round(percentChange, 4) * 100) & "%"
            Cells(summaryStock, 12).Value = totalSales
         
            summaryStock = summaryStock + 1
            currStock = Cells(I + 1, 1).Value
            openPrice = Cells(I + 1, 3).Value
            totalSales = 0
        End If
    Next I
    
    For I = 2 To (summaryStock)
        If Cells(I, 10).Value < 0 Then
            Cells(I, 10).Interior.ColorIndex = 3
        ElseIf Cells(I, 10).Value > 0 Then
            Cells(I, 10).Interior.ColorIndex = 4
            
        Else
            Cells(I, 10).Interior.ColorIndex = 0
        End If
    Next I
      
End Sub

