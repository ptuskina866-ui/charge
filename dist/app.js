'use strict';
const $ = (selector, parent = document) => parent.querySelector(selector);
const $$ = (selector, parent = document) => [...parent.querySelectorAll(selector)];
const menuButton = $('.menu-toggle');
const menu = $('#mobile-menu');
function closeMenu() { menu.hidden = true; menuButton.setAttribute('aria-expanded', 'false'); menuButton.setAttribute('aria-label', 'Открыть меню'); }
menuButton.addEventListener('click', () => { const open = menuButton.getAttribute('aria-expanded') !== 'true'; menu.hidden = !open; menuButton.setAttribute('aria-expanded', String(open)); menuButton.setAttribute('aria-label', open ? 'Закрыть меню' : 'Открыть меню'); });
$$('a', menu).forEach(a => a.addEventListener('click', closeMenu));
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
document.addEventListener('click', e => { if (!e.target.closest('.header')) closeMenu(); });

const powerValues = {8:'1,8',10:'2,2',13:'2,9',16:'3,5'};
$$('[data-current]').forEach(button => button.addEventListener('click', () => {
 $$('[data-current]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
 $('#power-output').innerHTML = `≈ ${powerValues[button.dataset.current]} <small>кВт</small>`;
 $('#power-fill').style.width = `${Number(button.dataset.current) / 16 * 100}%`;
}));

const leadDialog = $('#lead-dialog');
const legalDialog = $('#legal-dialog');
let returnFocus = null;
const form = $('#lead-form');
const message = $('#form-message');
function setFields(group, enabled, requiredNames = []) { group.hidden = !enabled; $$('input,textarea', group).forEach(input => {input.disabled = !enabled; input.required = enabled && requiredNames.includes(input.name);}); }
function openForm(type, trigger) {
 returnFocus = trigger; closeMenu(); form.reset(); message.hidden = true; $('#form-view').hidden = false; $('#success-view').hidden = true;
 const compatibility = type === 'compatibility'; const question = type === 'question';
 form.elements.requestType.value = type;
 setFields($('#order-fields'), !compatibility, ['name']);setFields($('#compat-fields'), compatibility, ['brand','model','year']);setFields($('#question-field'), question, ['question']);
 $('#form-title').textContent = compatibility ? 'Проверим ваш автомобиль.' : question ? 'Давайте разберёмся.' : 'Своя зарядка начинается здесь.';
 $('#form-description').textContent = compatibility ? 'Укажите автомобиль и удобный контакт. Поможем проверить зарядный разъём.' : question ? 'Оставьте вопрос и удобный способ связи.' : 'Оставьте контакты — поможем проверить совместимость и оформить заказ.';
 $('#submit-label').textContent = compatibility ? 'Проверить совместимость' : question ? 'Отправить вопрос' : 'Заказать';
 leadDialog.showModal(); document.body.classList.add('modal-open');
}
$$('[data-form]').forEach(button => button.addEventListener('click', () => openForm(button.dataset.form, button)));
$$('[data-close]').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
$$('dialog').forEach(dialog => { dialog.addEventListener('click', e => { const rect = dialog.getBoundingClientRect(); if (e.target === dialog && (e.clientX<rect.left||e.clientX>rect.right||e.clientY<rect.top||e.clientY>rect.bottom)) dialog.close(); }); dialog.addEventListener('close', () => { if (!document.querySelector('dialog[open]')) {document.body.classList.remove('modal-open');returnFocus?.focus({preventScroll:true});} }); });
$$('[data-legal]').forEach(button => button.addEventListener('click', () => {const privacy=button.dataset.legal==='privacy';$('#legal-title').textContent=privacy?'Политика конфиденциальности':'Реквизиты продавца';$('#legal-text').textContent=privacy?'[ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ]. Сведения об операторе и условия обработки персональных данных будут добавлены продавцом до начала приёма заявок.':'[РЕКВИЗИТЫ ПРОДАВЦА]. Наименование, регистрационные данные, адрес и контакты продавца будут добавлены до начала продаж.';legalDialog.showModal();document.body.classList.add('modal-open');}));
form.addEventListener('submit', async e => {
 e.preventDefault(); if (!form.reportValidity()) return;
 const endpoint = window.TESCHEV_CONFIG?.leadEndpoint;
 message.hidden = false;message.className='form-message';
 if (!endpoint) { message.textContent = 'Заявка не отправлена: приём заявок на сайте ещё не подключён. Ваши данные никуда не переданы.'; return; }
 if (!/^https:\/\//.test(endpoint) && !endpoint.startsWith('/api/')) {message.textContent='Отправка временно недоступна. Попробуйте позже.';return;}
 const submit = $('.submit-button', form); submit.disabled=true; message.textContent='Отправляем заявку…';
 try { const response=await fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(form))),signal:AbortSignal.timeout(15000)});const result=await response.json();if(!response.ok||result.ok!==true)throw new Error('Not accepted');$('#form-view').hidden=true;$('#success-view').hidden=false;$('#success-view .button').focus();form.reset(); }
 catch {message.textContent='Не удалось подтвердить отправку заявки. Попробуйте позже или свяжитесь с продавцом напрямую.';}
 finally {submit.disabled=false;}
});
const sticky = $('#sticky-order');
new IntersectionObserver(([entry]) => {const show=!entry.isIntersecting && entry.boundingClientRect.bottom<0;sticky.classList.toggle('is-visible',show);sticky.inert=!show;},{threshold:0}).observe($('#hero'));
if (!matchMedia('(prefers-reduced-motion: reduce)').matches) { const observer = new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-revealed');observer.unobserve(entry.target);}}),{threshold:.08});$$('.reveal').forEach(element=>{element.classList.add('will-reveal');observer.observe(element);}); }
$('#year').textContent = new Date().getFullYear();

const brandMarquee = $('.brand-marquee');

// Optional agent access to the same on-page controls. Does not submit contact data.
if (document.modelContext?.registerTool) {
 const lifecycle = new AbortController();
 const definitions = [{
  name:'configure_charging_current',title:'Выбрать режим зарядки',
  description:'Select 8, 10, 13 or 16 A in the visible illustrative power selector. Does not control a physical charger.',
  inputSchema:{type:'object',properties:{amps:{type:'integer',enum:[8,10,13,16]}},required:['amps'],additionalProperties:false},
  annotations:{readOnlyHint:false,untrustedContentHint:false},
  execute(input){if(!input||!Number.isInteger(input.amps)||![8,10,13,16].includes(input.amps))throw new Error('Expected amps: 8, 10, 13 or 16.');$(`[data-current="${input.amps}"]`).click();return{amps:input.amps,approximatePowerKw:powerValues[input.amps],voltage:220,illustrative:true};}
 },{
  name:'start_product_request',title:'Открыть форму Teschev',
  description:'Open the order, compatibility or question form. This only starts the flow; it does not send a lead.',
  inputSchema:{type:'object',properties:{type:{type:'string',enum:['order','compatibility','question']}},required:['type'],additionalProperties:false},
  annotations:{readOnlyHint:false,untrustedContentHint:false},
  execute(input){if(!input||!['order','compatibility','question'].includes(input.type))throw new Error('Unknown request type.');if(legalDialog.open)legalDialog.close();if(leadDialog.open)leadDialog.close();openForm(input.type,document.activeElement);return{form:input.type,status:'opened',submissionAvailable:Boolean(window.TESCHEV_CONFIG?.leadEndpoint)};}
 }];
 definitions.forEach(definition=>{try{Promise.resolve(document.modelContext.registerTool(definition,{signal:lifecycle.signal})).catch(()=>{});}catch{}});
 window.addEventListener('pagehide',()=>lifecycle.abort(),{once:true});
}
