html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The report</title>
    <style>
        .container{
            justify-content: center;
            align-items: center;
            position: relative;

        }
        .justify-center{
            justify-content: center;
        }
        .items-center{
            align-items: center;
        }
        .relative{
            position: relative;
        }
        .flex{
            display: flex;
        }
        .flex-row{
            flex-direction: row;
        }
        .flex-col{
            flex-direction: column;
        }
        .space-around{
            justify-content: space-around;
        }
        li{
            list-style-type: none;
            border-radius: 0.25rem;
            margin-bottom: 6px;
        }
        .p-1{
            padding: .25rem;
        }
        .p-2{
            padding: .5rem;
        }
        .r-1{
            border-radius: 0.25rem;
        }
        .w-30{
            width: 30%;
        }
        .stat{
            width: 80%;
        }
        .gap-1{
            gap: 1 0;
        }
        .record-list{
            width: 80%;
        }
        .list-item{
            padding: 4px;
            border: 3px;
        }
        .status{
            font-weight: bold;
        }
        .status-servival{
            color: hsl(125.31deg 62.03% 46.47%);
            background-color: hsl(125.31deg 62.03% 46.47% / 14.9%);
        }
        .status-deaed{
            color: hsl(0deg 63.43% 53.06%);
            background-color: hsl(0deg 63.43% 53.06%/14.9%);
        }
        .status-reject{
            color: hsl(0deg 0% 60.16%);
            background-color: hsl(0deg 0% 60.16%/14.9%);
        }
    </style>
    <script>
        var reportData = {{}}
    </script>
</head>
<body>
    <p style = "text-align:center"><img src="data:image/png;base64,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" /></p>
	<p style = "text-align:center">Out Success!</p>
	<p style = "text-align:center">By <a href="https://github.com/AabyssZG">曾哥(AabyssZG)</a> && <a href="https://github.com/jingyuexing">jingyuexing</a></p>
    <div class="container relative flex flex-col">
        <div class="stat flex space-around">
        </div>
        <ul class="record-list">
        </ul>
    </div>
    <script>
        function createRecord(item){
            let listItem = document.createElement("li")
            listItem.classList.add("list-item","flex","space-around")
            let urlRecord = document.createElement("div")
            urlRecord.innerText = item.url
            urlRecord.classList.add("link","w-30","flex","items-center")
            let statusCode = document.createElement("div")
            statusCode.innerText = item.statusCode
            statusCode.classList.add("w-30","flex","justify-center")
            let state = document.createElement("div")
            state.classList.add("status","w-30","flex","items-center")
            state.innerText = item.status
            let itemType = ""
            switch(item.status){
            case "deaed":
                itemType = "status-deaed"
                break
            case "reject":
                itemType = "status-reject"
                break
            case "servival":
                itemType = "status-servival"
                break
            }
            listItem.classList.add(itemType)
            listItem.appendChild(urlRecord)
            listItem.appendChild(statusCode)
            listItem.appendChild(state)
            return listItem
        }
        let recordList = document.getElementsByClassName("record-list")[0]
        let stat = document.getElementsByClassName("stat")[0];
        let Count = [reportData.filter(item=>item.status === "servival").length,reportData.filter(item=>item.status === "reject").length,reportData.filter(item=>item.status === "deaed").length];
        let statName =["servival","reject","deaed"]
        for(let idx in Count){
            let box = document.createElement("div")
            let title = document.createElement("span")
            title.innerText = statName[idx]+":"
            let nums = document.createElement("span")
            nums.innerText = Count[idx]
            box.classList.add("status-"+statName[idx],"p-2","r-1")
            box.appendChild(title)
            box.appendChild(nums)
            stat.append(box)
        }
        for(let item of reportData){
            recordList.appendChild(createRecord(item))
        }
    </script>
</body>
</html>
'''

def generaterReport():
    global html
    data = ""
    with open(".data/report.json",encoding="utf-8",mode="r+") as file:
        data = file.read()
    html = html.replace("{{}}",data)
    with open("report.html",encoding="utf-8",mode="+w") as file:
        file.write(html)

if __name__ == '__main__':
    generaterReport()
