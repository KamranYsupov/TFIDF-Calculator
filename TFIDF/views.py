from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .service import clean_word, calculate_tf, calculate_idf


def redirect_from_main_page(request):
    return redirect('tfidf')


def upload_files(request):
    if request.method == 'POST' and request.FILES:
        files = request.FILES.getlist('files')
        file_contents = []
        for file in files:
            fs = FileSystemStorage('media/text_files')
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.path(filename)
            with open(uploaded_file_url, 'r', encoding='utf-8') as f:
                file_contents.append(f.read())

        tfidf_results = []
        for i, doc in enumerate(file_contents):
            tfidf_dict = {}
            words = set(doc.split())
            for word in words:
                tf = calculate_tf(clean_word(word), doc)
                idf = calculate_idf(clean_word(word), file_contents)
                tfidf = tf * idf
                tfidf_dict[clean_word(word)] = {'tf': tf, 'idf': idf, 'tfidf': tfidf}
            tfidf_results.append(tfidf_dict)

        return render(request, 'TFIDF/index.html', {'tfidf_results': tfidf_results})
    return render(request, 'TFIDF/index.html')
