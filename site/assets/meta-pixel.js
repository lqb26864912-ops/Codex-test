/* Meta Pixel for magnificentvisa.com
 * 1. Put the Pixel ID (numbers only, from Meta Events Manager) in PIXEL_ID below.
 *    While it is empty this script does nothing.
 * 2. Events sent:
 *    PageView – every page
 *    Contact  – click on WhatsApp / Telegram / LINE / Messenger links, or the copy-WeChat button
 *    Lead     – the inquiry form's final "send" step (WhatsApp / Telegram / copy text)
 *    Each event carries channel, service (from the page path) and page language.
 */
(function () {
  'use strict';
  var PIXEL_ID = '1442570674148916';
  if (!/^\d{6,20}$/.test(PIXEL_ID)) return;

  /* Standard Meta Pixel base code */
  !function (f, b, e, v, n, t, s) {
    if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
    if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
    t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
  }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', PIXEL_ID);
  fbq('track', 'PageView');

  var lang = (document.documentElement.lang || 'zh').slice(0, 2);
  var path = location.pathname.replace(/^\/(en|th)\//, '/');
  var service = path === '/' || path === '/index.html' ? 'home'
    : path.indexOf('/news/') === 0 ? 'news'
    : path.indexOf('/tools/') === 0 ? 'visa-checker'
    : path.replace(/^\//, '').replace(/\.html$/, '') || 'home';

  var CHANNELS = [['wa.me', 'whatsapp'], ['t.me', 'telegram'], ['line.me', 'line'], ['m.me', 'messenger']];
  function channelOf(href) {
    for (var i = 0; i < CHANNELS.length; i++) if (href.indexOf('//' + CHANNELS[i][0] + '/') !== -1) return CHANNELS[i][1];
    return null;
  }
  function send(event, channel) {
    fbq('track', event, { content_name: channel, content_category: service, language: lang });
  }

  document.addEventListener('click', function (e) {
    var el = e.target && e.target.closest ? e.target.closest('a[href], [data-copy-wechat], button') : null;
    if (!el) return;
    var inForm = !!el.closest('#inquiry-form, #inquiry-result');
    if (el.hasAttribute('data-copy-wechat')) return send('Contact', 'wechat');
    if (el.tagName === 'A') {
      var ch = channelOf(el.href || '');
      if (!ch) return;
      return send(inForm ? 'Lead' : 'Contact', ch);
    }
    /* "Copy text" button on the last step of the inquiry form */
    if (inForm && el.id === 'copy-inquiry') send('Lead', 'copy');
  }, true);
})();
