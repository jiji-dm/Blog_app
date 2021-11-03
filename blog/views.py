from django.db.models.query import QuerySet
from django.views import generic    #django.views.generic.base.TemplateView
from .models import BlogPost
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages


class IndexView(generic.ListView):
    #トップページのビュー

    template_name = 'index.html'
    """
        template_nameはTempalateResponseMixinで定義されている変数である
        オーバーライド(再定義)することで任意のテンプレートをレンダリングする
        注意)　Template_nameはファイルしか設定できない
                Djangoが参照してくれるのはtemplateが格納しているフォルダのみ[templates]
    """
    context_object_name = 'orderby_records'
    queryset= BlogPost.objects.order_by('-posted_at')
    #モデルBlogPostのオブジェクトにorder_by()を適用して
    #BlogPostのレコードを投稿日時の降順を並べ替える
    """
    Attributes:
        template_name:レンタリングするテンプレート
        context_object_name:object_listキーの別名を設定　obuject_list → 変更　参照名変更
        queryset:データベースのクエリ
    """
    paginate_by = 4
    #1ページに表示するレコードの件数
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class BlogDetail(generic.DetailView):
    #詳細ページのビュー
    """
        投稿記事の詳細を表示するためDetailViewを継承する。
        Attributes
        template_name: レンダリングするテンプレート
        Model: モデルのクラス
    """
    template_name = 'post.html'
    model = BlogPost
    #クラス変数のmodelにモデルBlogPostを設定する。

class ScienceView(generic.ListView):
    template_name = 'science_list.html'
    model = BlogPost
    context_object_name = 'science_records'
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    paginate_by = 2

class DailylifeView(generic.ListView):
    template_name = 'dailylife_list.html'
    model = BlogPost
    context_object_name = 'dailylife_records'
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    paginate_by = 2

class MusicView(generic.ListView):
    template_name = 'music_list.html'
    model = BlogPost
    context_object_name = 'music_records'
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    paginate_by = 2

class ContactView(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
