window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');    
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

    function onRowClick() {
        alert('hello')
    }
    const img_slider = document.getElementById('img-slider');    

    const datatablesSimple2 = document.getElementById('datatablesSimple2');
    if (datatablesSimple2) {        
        new simpleDatatables.DataTable(datatablesSimple2, {
            searchable: false,
            perPage: 5,
            paging: false,             
        });
        function fnImgPop(url){
            var img=new Image();
            img.src=url;
            var img_width=img.width/2;
            var win_width=(img.width+25)/2;
            var img_height=img.height/2;
            var win=(img.height+30)/2;

            // var img_width=img.width;
            // var win_width=img.width+25;
            // var img_height=img.height;
            // var win=img.height+30;
            var OpenWindow=window.open('','_blank', 'width='+img_width+', height='+img_height+', menubars=no, status=no,toolbar=no,scrollbars=no');            
            OpenWindow.document.write("<style>body{margin:0px;}</style><img src='"+url+"' width='"+win_width+"'>");
            OpenWindow.document.title='Detect Image';
        }
        
        datatablesSimple2.addEventListener('click', function (e) {
            for (let t = e.target; t && t != this; t = t.parentNode) {
                if (t.matches("#datatablesSimple2 tbody tr td")) {
                    // console.log(t.getAttributeNames())
                    // console.log(t.getAttribute('id'))
                    // fnImgPop("/static/images/"+ t.getAttribute('id'))  #Noti이미지 팝업창처리.
                    // $.ajax({
                    //     type: "GET",
                    //     url: "/api_notifySelect?id="+t.getAttribute('id'),                
                    //     dataType: "json",
                    //     success: function (data) {   
                    //         console.log(data);              
                    //         var apiTest = "";
                    //         for (var i = 0; i < data.length; i++) {                        
                    //             apiTest += "<li class='mis-slide'>"
                    //             apiTest += "<img src='" + data[i].fields.img_name + " width='1000' height='700'>"
                    //             apiTest += "</li>"
                    //         }
                    //         $('[id="img-slider"]').html(apiTest);
                    //     },
                    //     error: function (request, status, error) {
                    //         console.log('실패');
                    //     }
                    // })
                    // GET 방식으로 서버에 HTTP Request를 보냄. 
                    $.get(
                        "/api_notifySelect", 
                        { id: t.getAttribute('id')}, // 서버가 필요한 정보를 같이 보냄. 
                        function(data, status) {
                            // 전송받은 데이터와 전송 성공 여부를 보여줌. 
                            var imgStr = String(data[0].fields.img_name);      
                            var apiTest = "";
                            for (var i = 0; i < data.length; i++) {     
                                // apiTest += "<ol class='mis-slider' id='mis-solo'>"                   
                                apiTest += "<li class='mis-slide' id='slider_id'>"
                                apiTest += "<img src='/static/images/"+ imgStr + "' width='1000' height='700'>"
                                apiTest += "</li>"
                                // apiTest += "</ol>"
                            }
                            $('[id="solo_id"]').html(apiTest);
                        }, "json"
                        ); 
                    // 5초후 호출.
                    timer = setTimeout( function() {
                        // $.ajax({
                        //     url: "/api_notify",
                        //     dataType: "json",
                        //     success: function (data) {
                        //         var apiTest = "";
                        //         // apiTest += "<ol class='mis-slider'>"
                        //         for (var i = 0; i < data.length; i++) {                
                        //             apiTest += "<li class='mis-slider' id='mis-sldier'>"                                            
                        //             apiTest += "<img src='/static/images/"+ data[i].fields.img_name + "' width='1000' height='700'>"                                    
                        //             apiTest += "</li>"
                        //         }
                        //         // apiTest += "</ol>"                                
                        //         $('[id="img-solo"]').html(apiTest);
                        //     },
                        //     error: function (request, status, error) {
                        //         console.log('실패');
                        //     }
                        // })
                        window.location.reload()
                    }, 5000);
                    break
                }
            }
            
        }, false)
    }

    

    
});
