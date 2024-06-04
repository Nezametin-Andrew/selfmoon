$(document).ready(function(){

    let iconShowClassName = 'bi bi-eye-slash-fill';
    let iconHideClassName = 'bi bi-eye-fill';


    showWordList = (id, lst) =>{
        for(let i = 1; i <= 3; i++){
            if(i == lst){
                if($(`#show-icon-${i}`).attr('class')  == iconShowClassName){
                    $(`#show-icon-${i}`).attr('class', iconHideClassName);
                    $("#card-word-list").load(`${baseUrl}seo/get_list_word_for_sort/${id}/${lst}/`);
                }else{
                    $(`#show-icon-${i}`).attr('class', iconShowClassName);
                    $("#card-word-list").empty();
                };
            }else{
                $(`#show-icon-${i}`).attr('class', iconShowClassName);
                $("#card-word-list").empty();
            }
        }
        
    };




});
