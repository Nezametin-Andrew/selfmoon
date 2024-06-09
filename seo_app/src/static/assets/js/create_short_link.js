var amountLink = 1;
var tooltip = null;
var currentTarget = null;

function validateAndAddLink() {
    if (validateForm(amountLink - 1)) {
        addLink(amountLink);
    }
}

function validateForm(amoLink) {
    let isValid = true;
    $(`#flush-collapse${amoLink} input[type="text"], #flush-collapse${amoLink} textarea`).each(function() {
        console.log(this)
        let optional = $(this).data("optional");
        let value = $(this).val().trim();
        console.log('Optional:', optional, 'Value:', value); 
        if (optional === undefined || optional === false) {
            if (value === "") {
                isValid = false;
            }
        }
    });
    if (!isValid) {
        $('#validation-form').addClass('show');
    }
    return isValid;
}

function hideAlert () { 
    $('#validation-form').removeClass('show');
 }


function addLink(amoLink) {
    let html = `
        <div class="accordion-item">
            <h2 class="accordion-header" id="flush-heading${amoLink}">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse${amoLink}" aria-expanded="false" aria-controls="flush-collapse${amoLink}">
                    Ссылка: ${amoLink}
                </button>
            </h2>
            <div id="flush-collapse${amoLink}" class="accordion-collapse collapse" aria-labelledby="flush-heading${amoLink}" data-bs-parent="#accordionFlushExample">
                <div class="accordion-body">
                    <div class="row mb-4">
                        <label for="link_service${amoLink}" class="col-sm-3 col-form-label">
                            <span style="display: inline-block; margin-right: 5px; cursor: pointer; color: gray; font-size: 16px; font-weight: bolder;">
                                <i class="bi bi-info-circle" data-tooltip="Нажмите, чтобы получить больше информации" data-bs-toggle="modal" data-bs-target="#verticalycentered"></i>
                                <div class="modal fade" id="verticalycentered" tabindex="-1" aria-hidden="true" style="display: none;">
                                <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                    <div class="modal-header">
                                    <h5 class="modal-title">Ссылка сервиса:</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                    Нужно указать прямую ссылку на сервис, по сокращению ссылок, например: https://example.com
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </span>Ссылка сервиса:
                        </label>
                        <div class="col-sm-9">
                            <input type="text" name="link_service${amoLink}" class="form-control" >
                        </div>
                    </div>
                    <div class="row mb-4">
                        <label for="link_default${amoLink}" class="col-sm-3 col-form-label">
                                <span style="display: inline-block; margin-right: 5px; cursor: pointer; color: gray; font-size: 16px; font-weight: bolder;">
                                <i class="bi bi-info-circle" data-tooltip="Нажмите, чтобы получить больше информации" data-bs-toggle="modal" data-bs-target="#verticalycentered2"></i>
                                <div class="modal fade" id="verticalycentered2" tabindex="-1" aria-hidden="true" style="display: none;">
                                <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                    <div class="modal-header">
                                    <h5 class="modal-title">Ссылка по умолчанию:</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                    Ссылка по умолчанию, нужно взять вашу уникальную ссылку и сократить ее, эта поле обязательно для заполнения. Ваша уникальная ссылка: <span id='uniq_link${amoLink}'> </span>
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </span>
                        Ссылка по умолчанию:</label>
                        <div class="col-sm-9">
                            <input type="text" name="link_default${amoLink}" class="form-control">
                            <input type='hidden' name='default-link${amoLink}' >
                        </div>
                    </div>
                    <div class="row mb-4">
                        <label for="link_api${amoLink}" class="col-sm-3 col-form-label">
                                <span style="display: inline-block; margin-right: 5px; cursor: pointer; color: gray; font-size: 16px; font-weight: bolder;">
                                <i class="bi bi-info-circle" data-tooltip="Нажмите, чтобы получить больше информации" data-bs-toggle="modal" data-bs-target="#verticalycentered3"></i>
                                <div class="modal fade" id="verticalycentered3" tabindex="-1" aria-hidden="true" style="display: none;">
                                <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                    <div class="modal-header">
                                    <h5 class="modal-title">Ссылка API:</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                    Ссылка на API вашего сервиса по сокращению ссылок, нужно для генерации новых ссылок, чтобы каждый исполнитель проходил по уникальной ссылке 1 исполнитель = 1 ссылка. Ваши данные не передаются третьим лицам! Если сервис не предоставляет APi, то будет использована ссылка по умолчанию.
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </span>
                        Ссылка API:</label>
                        <div class="col-sm-9">
                            <input type="text" name="link_api${amoLink}" class="form-control" data-optional="true">
                        </div>
                    </div>
                    <div class="row mb-4">
                        <label for="description_l${amoLink}" class="col-sm-3 col-form-label">
                                <span style="display: inline-block; margin-right: 5px; cursor: pointer; color: gray; font-size: 16px; font-weight: bolder;">
                                <i class="bi bi-info-circle" data-tooltip="Нажмите, чтобы получить больше информации"  data-bs-toggle="modal" data-bs-target="#verticalycentered4"></i>
                                <div class="modal fade" id="verticalycentered4" tabindex="-1" aria-hidden="true" style="display: none;">
                                <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                    <div class="modal-header">
                                    <h5 class="modal-title">Общее описание:</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                    Напишите краткую инструкцию, как исполнитель должен пройти задание, инструкция - повысит уровень качества прохождения, для наглядности, вы можете добавить изображения.
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </span>
                        Общее описание:</label>
                        <div class="col-sm-9">
                            <textarea class="form-control" name="description_l${amoLink}" style="height: 120px; resize: none;" id="editor${amoLink}" data-optional="true"></textarea>
                        </div>
                    </div>
                    <div class="col-sm-9">
                        <div class="form-check form-switch">
                            
                            <label class="form-check-label" for="flexSwitchCheckDefault${amoLink}">
                                                        <span style="display: inline-block; margin-right: 5px; cursor: pointer; color: gray; font-size: 16px; font-weight: bolder;">
                                <i class="bi bi-info-circle" data-tooltip="Нажмите, чтобы получить больше информации" data-bs-toggle="modal" data-bs-target="#verticalycentered5"></i>
                                                            <div class="modal fade" id="verticalycentered5" tabindex="-1" aria-hidden="true" style="display: none;">
                                <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                    <div class="modal-header">
                                    <h5 class="modal-title">alias для API:</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                    Указывается в том случае, если вы указали ссылку для API и в этой ссылке есть параметр alias.
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                </div>
                            </div>
                                </span>
                            Нужен alias для API?</label>
                            <input class="form-check-input" name="alias${amoLink}" type="checkbox" id="flexSwitchCheckDefault${amoLink}" data-optional="true">
                        </div>
                    </div>
                    <div class="col-sm-9" style="margin-top: 20px;">
                        <a  class="btn btn-success" onclick="validateAndAddLink()">Готово</a>
                    </div>
                </div>
            </div>
        </div>
    `;

    $('#accordionFlushExample').append(html);

    $.post(
        '/short_link/create_link_template/',
        {},
        function (data){
            if(data.short_link != ''){
                let element = document.getElementById(`uniq_link${amoLink}`);
                let inputElement = document.querySelector(`input[name='default-link${amoLink}']`);
                
                if (element && inputElement) {
                    element.innerText = data.short_link;
                    inputElement.value = data.short_link;

                } else {
                    console.error(`Element uniq_link${amoLink} not found`);
                }
            }
        }
    )

    addCkeditor(amoLink);
    amountLink++;
}

function addCkeditor(amoLink) {
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

document.addEventListener('DOMContentLoaded', function() {
    addLink(amountLink);

    document.body.addEventListener('mouseenter', function(event) {
        if (event.target.matches('[data-tooltip]')) {
            const target = event.target;
            const message = target.getAttribute('data-tooltip');
            currentTarget = target;
            tooltip = createTooltip(target, message);
            updateTooltipPosition(target);
            window.addEventListener('scroll', updateTooltipPosition);
            setTimeout(() => {
                tooltip.classList.add('show');
            }, 0);
        }
    }, true);

    document.body.addEventListener('mouseleave', function(event) {
        if (event.target.matches('[data-tooltip]')) {
            if (tooltip) {
                tooltip.classList.remove('show');
                setTimeout(() => {
                    if (tooltip && tooltip.parentNode) {
                        tooltip.parentNode.removeChild(tooltip);
                        tooltip = null;
                        window.removeEventListener('scroll', updateTooltipPosition);
                    }
                }, 300);
            }
        }
    }, true);
});

function createTooltip(target, message) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.innerText = message;
    document.body.appendChild(tooltip);

    return tooltip;
}

function updateTooltipPosition() {
    if (tooltip && currentTarget) {
        const targetRect = currentTarget.getBoundingClientRect();
        tooltip.style.left = `${targetRect.right + 10}px`;
        tooltip.style.top = `${targetRect.top + window.scrollY + (targetRect.height / 2) - (tooltip.clientHeight / 2)}px`;
    }
}
// document.addEventListener('DOMContentLoaded', function() {
//     var testAd = document.createElement('script');
//     testAd.type = 'text/javascript';
//     testAd.src = 'https://example.com/ad.js'; // URL, который блокируется блокировщиками рекламы
//     testAd.onerror = function() {
//         var adblockMessage = document.getElementById('adblock-message');
//         adblockMessage.style.display = 'block';
//     };
//     document.body.appendChild(testAd);
// });



