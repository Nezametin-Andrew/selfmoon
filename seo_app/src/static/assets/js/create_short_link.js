var amountLink = 1;


function addLink(amoLink){
    let html = `
        <div class="accordion-item">
            <h2 class="accordion-header" id="flush-heading${amoLink}">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse${amoLink}" aria-expanded="false" aria-controls="flush-collapse${amoLink}">
                    Ссылка: ${amoLink}
                </button>
            </h2>
            <div id="flush-collapse${amoLink}" class="accordion-collapse collapse" aria-labelledby="flush-heading${amoLink}" data-bs-parent="#accordionFlushExample" style="">
                <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.</div>
                </div>
            </div>
    `

    $('#accordionFlushExample').append(html);
}

//addLink(amountLink);


function addCkeditor(amoLink){
    ClassicEditor
    .create(document.querySelector(`#editor${amoLink}`), {
        toolbar: {
            items: [
                'heading', '|',
                'bold', 'italic', 'bulletedList', 'numberedList', 'blockQuote', '|',
                'undo', 'redo', '|',
                'imageUpload'
            ]
        },
        ckfinder: {
            uploadUrl: '/ckeditor/upload/'
        }
    })
    .then(editor => {
        console.log(editor);
    })
    .catch(error => {
        console.error(error);
    });
}