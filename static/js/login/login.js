
function save() {
    debugger
 	  itemlist={'username':$("#username").val(),'password':$("#password").val(),'check':$("#checkmy").is(':checked')}
 	  //发送请求
       $.post({
            url:'/save/',
            headers:{"X-CSRFToken":$.cookie('csrftoken')}, //在请求头部加入django生成的cref_token
            data: itemlist,
            // contentType:'application/json',
            success:function (data)
            {
                if(data.code==500)
                {
                   layer.alert('请填写正确的用户名和密码')
                }else{
                     location.href= '/Home/'
                }
            }
       })
}
