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
