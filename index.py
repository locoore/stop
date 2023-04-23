from flask import Flask, request, render_template, url_for
import openai

index = Flask(__name__)

@index.route("/")
def bass():
    image_url = url_for('static', filename='/ima/logo1.png')
    image1 = 'https://i.imgur.com/PWfUkS8'
    return f"""
        <!DOCTYPE html>
        <html>
          <head>
            <title>放棄規劃提問</title>
            <link rel="icon" type="image/png" href="{image_url}">

            <style>
              /* 設置區塊背景色、將區塊置中 */
              
              .toto {{
                background-color:#445678;
                float: left;
                text-align: center;
                margin: auto;
                width: 2%;
                padding: 55px;
              }}
              
              .tosa {{
                  display: flex;
                  justify-content: center; /* 水平置中 */
                  align-items: center; /* 垂直置中 */
              }}
              
              
              .coco {{
                background-color:#3b4d6e;
                text-align: center;
                margin: auto;
                width: auto;
                padding: 8px;
                font-size: 25px;
                color: #cc5e3f;
              }}
              
              .coco1 {{
                background-color:#445678;
                text-align: center;
                margin: auto;
                width: auto;
                padding: 3px;


              }}
              

              .lili {{
                text-align: center;
                
                margin: auto;
                width: 100px;
                padding: 55px;

              }}
              
              .lili1 {{
                background-color:#445678;
                text-align: center;
                margin: auto;
                width: auto;
                padding: 8px;
                color: #24100a;
              }}
              
              .pack1 {{
                  display: flex;
                  }}
              
              
              .tete {{
                  display: flex;
                  background-color:#dec0b8;
                  width: 500px;
                  padding: 55px;
                  
                  }}
              
              .tete1 {{
                  font-size: 10px;
                  float: left;
                  text-align: left;
                  color: #24100a;
                  }}
              
              .tetea {{
                  display: flex;
                  background-color:#cfbab4;
                  width: 55px;
                  padding: 55px;
                  
                  }}
              
              .teteb {{
                  display: flex;
                  background-color:#bdaca8;
                  width: 1px;
                  padding: 55px;
                  
                  }}
              
              /* 更改背景顏色 */
              body {{
                background-color: #677182;
                
                font-family: "俐方體11号", Arial, sans-serif;
              }}
                                      
            </style>
          </head>
          <body>
          

          

          

    
          <div class="coco">
                              
          <b> <p>放棄規劃提問</p></b>
          </div>
          
          <div class="coco1">
                              
          <b> <p></p></b>
          </div>
          

            
        <div class="toto">
  
            <div class="tosa">
              <!-- 插入圖像 -->
              <img src="{image_url}" alt="logo1" width=110 height=110>   
            </div>

        </div>
          
<div class="pack1">
            
            <div class="tete">
            <div class="tete1">
            <h1>
            提供給對將來猶豫者的服務，
            <p>
            只要將問題輸入，便能獲得一定程度的答案。
            </h1>
            </div>
            </div>
            
            <div class="tetea">
                        </div>
                        
                        <div class="teteb">
                                    </div>
            
            <br>
            



            <div class="lili">
            <a href="/luck">提問介面</a>
            </div>


</div>
            <div class="lili1">
            <p></p>
            </div>

          </body>
        </html>
    """

@index.route("/luck", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 從表單中獲取 name、sex、star
        name = request.form["name"]
        sex = request.form["sex"]
        star = request.form["star"]

        # 組合提示語
        if sex == "男":
            prompt = f"假設你是一位專業的星座專家，現在有一位顧客，他叫做{name}，他的性別是{sex}，他的星座是{star}，請用繁體中文說明他這一周的財富運勢。"
        else:
            prompt = f"假設你是一位專業的星座專家，現在有一位顧客，她叫做{name}，她的性別是{sex}，她的星座是{star}，請用繁體中文說明她這一周的愛情運勢。"

        # 調用 OpenAI API 獲取運勢信息
        openai.api_key = "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"
        chat_output = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.5,
            max_tokens=128,
            n=1,
            stop=None,
            timeout=60,
        )
        # 獲取回應信息
        re_content = chat_output.choices[0].text.strip()

        # 返回運勢信息
        return f"一周運勢：{re_content}"
    else:
        # 顯示表單供用戶輸入
        return """
            <form method="post">
                <label for="name">姓名：</label>
                <input type="text" name="name" required><br>

                <label for="sex">性別：</label>
                <select name="sex" required>
                    <option value="男">男</option>
                    <option value="女">女</option>
                </select><br>

                <label for="star">星座：</label>
                <input type="text" name="star" required><br>

                <input type="submit" value="提交">
            </form>
        """

if __name__ == "__main__":
    index.run(port=8000)
