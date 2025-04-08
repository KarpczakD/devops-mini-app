# DevOps Mini App

## Opis projektu

Aplikacja to prosta aplikacja webowa oparta na Flask, która demonstruje podstawy DevOps. Projekt jest zbudowany przy użyciu Dockera i GitHub Actions. Aplikacja umożliwia logowanie, zmianę hasła, kontakt przez formularz oraz wyświetlanie wiadomości kontaktowych. Projekt służy jako przykład implementacji CI/CD oraz testowania aplikacji webowych.

## Instalacja

Aby zainstalować aplikację i uruchomić ją lokalnie, wykonaj poniższe kroki:

### Wymagania
- Python 3.x
- Docker (opcjonalnie, jeżeli chcesz uruchomić aplikację w kontenerze)

### Krok 1: Klonowanie repozytorium
Klonuj repozytorium na swoje lokalne urządzenie:
```
git clone https://github.com/karpik3004/devops-mini-app.git
cd devops-mini-app
```
### Krok 2: Instalacja zależności
Zainstaluj wymagane pakiety:
```
pip install -r requirements.txt
```
### Krok 3: Uruchomienie aplikacji lokalnie
Uruchom aplikację lokalnie:
```
python app.py
```
Aplikacja będzie dostępna pod adresem: `http://localhost:5000`.

### Krok 4: Uruchomienie aplikacji za pomocą Dockera (opcjonalnie)
Jeśli chcesz uruchomić aplikację w kontenerze Docker, upewnij się, że masz zainstalowany Docker. Następnie uruchom poniższe polecenia:
```
docker-compose up --build
```
## Użycie

Aplikacja składa się z kilku stron:

1. **Strona główna**: Główna strona aplikacji, na której można przejść do logowania, zmiany hasła lub wiadomości kontaktowych.
2. **Formularz kontaktowy**: Pozwala użytkownikowi wysłać wiadomość. Po wysłaniu formularza użytkownik zostanie przekierowany z komunikatem o sukcesie lub błędzie.
3. **Strona logowania**: Umożliwia zalogowanie się na konto administratora.
4. **Zmiana hasła**: Formularz umożliwiający zmianę hasła.

Po wypełnieniu formularza kontaktowego użytkownik zostanie przekierowany na stronę kontaktową z odpowiednim komunikatem.

## Testy

Aplikacja zawiera zestaw testów jednostkowych opartych na frameworku `pytest`. Aby uruchomić testy, użyj poniższego polecenia:
```
pytest
```
Testy obejmują m.in.:
- Sprawdzenie strony głównej.
- Testowanie formularza kontaktowego.
- Testowanie strony logowania.
- Testowanie zmiany hasła.

## Przykłady

Przykład testowania formularza kontaktowego:
1. Wypełnij formularz na stronie kontaktowej.
2. Zatwierdź formularz.
3. Zostaniesz przekierowany na stronę kontaktu z komunikatem o powodzeniu lub błędzie.

## Licencja

Ten projekt jest dostępny na licencji MIT. Możesz go używać, modyfikować i dystrybuować zgodnie z warunkami licencji MIT.
