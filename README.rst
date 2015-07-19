===============================================
Problems when learning Django Blog Zinnia
===============================================

1. models_bases
===============

Search google and record some founds.

 * 1.1 django.db.models import Q
 
 Q objects are used for complex queries(for example involving AND, OR statements).
 Poll.objects.filter(Q(question_contains='keyword1'))
 Poll.objects.filter(Q(question_contains='keyword1') & Q(question_contains='keyword2'))
 #no logic is the same as and
 Poll.objects.filter(Q(question__contains='dinner'), Q(question__contains='meal'))
 #(A OR B) AND C
 Poll.objects.filter((Q(question__contains='key1') | Q(question__contains='key2')) & Q(pub_date=datetime.date.today()))
 
 * 1.2 django.utils.text import Truncator
 
 trun = Truncator('this may be a such long long text')
 >>> trun.chars(7)
 u'this...'
 >>>trun.chars(7, truncate='--')
 u'this --'
 >>>trun.chars(7, truncate='> %(truncated_text)s...')
 u'> th...'
 
 * 1.3 django.utils.html import strip_tags
 
 Strip HTML tags.
 
 >>>html='<p>paragraph</p>'
 
 >>>stripped = strip_tags(html)
 u'paragraph'
 
 {{ template | striptags }}
 
 * 1.4 django.utils.html import linebreaks
 
 Convert plain text to include html line breaks
 
 * 1.5 django.template.defaultfilters import removetags
 
 html = '<strong>Bold...</strong><p>paragraph....</p>'
 removetags(html, 'strong')
 removetags(html, 'strong p')
 {{ template | removetags:"a span" | safe }}
