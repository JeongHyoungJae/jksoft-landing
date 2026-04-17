# AI Agent 작업 시 파일 인코딩(한글 깨짐) 발생 원인 및 주의사항

AI Agent가 코드를 수정하는 과정에서 간헐적으로 한글 등 멀티바이트 문자의 인코딩이 깨지는 현상이 발생할 수 있습니다. 해당 현상의 정확한 원인과 예방/해결 가이드를 아래에 기록합니다.

## 1. 인코딩 깨짐 발생 원인
Agent는 다중 라인 문자열이나 복잡한 구조를 수정할 때 내부 툴(`replace_file_content`) 대신 시스템 명령어인 Windows PowerShell (`Set-Content`, `>` 등)을 활용하여 정규식(Regex)을 통한 일괄 변경을 시도할 때가 있습니다.

이때 **Windows 기반의 PowerShell 5.1 환경**에서는 파일 저장 시 인코딩 파라미터를 명시하지 않으면 기본적으로 **ANSI (System Default, 한국어 윈도우의 경우 EUC-KR/CP949)** 형태로 파일을 저장합니다. 
웹 개발 표준인 **BOM 없는 UTF-8 (UTF-8 without BOM)** 로 작성되어 있던 원본 HTML/JS 파일들이 PowerShell의 기본 동작에 의해 ANSI로 강제 변환·저장되며, 이 과정에서 UTF-8을 기대하는 에디터나 브라우저, 내부 파서가 이를 읽지 못해 **"인코딩 깨짐(글꼴 뭉개짐)"** 오류가 발생하게 됩니다.

## 2. Agent 작업 지침 (해결 및 예방 가이드)

향후 같은 문제를 방지하기 위해 Agent는 파일 수정 시 다음 원칙을 절대적으로 준수해야 합니다.

### 원칙 A: 기본 내장 툴 우선 사용 
가능한 한 운영체제의 셸 환경에 의존하지 않고, Agent에게 제공된 `multi_replace_file_content` 또는 `replace_file_content` 툴을 사용합니다. 해당 내장 툴들은 내부적으로 크로스 플랫폼 UTF-8 입출력을 안전하게 처리합니다.

### 원칙 B: PowerShell 사용 시 `.NET` 클래스 강제 활용
만약 불가피하게 정규식 매칭 등 PowerShell 커맨드를 통해 텍스트를 처리하고 저장해야 할 경우, 절대로 `Set-Content`나 꺾쇠(`>`) 리다이렉션을 사용해서는 안 됩니다 (PowerShell 5.1의 `-Encoding UTF8` 옵션은 쓸데없는 BOM을 파일 맨 앞에 추가하는 부작용이 있습니다). 
반드시 다음과 같이 `.NET`의 `System.IO.File` 클래스와 `UTF8Encoding($false)`를 통해 BOM 없는 순수 UTF-8로 저장해야 합니다.

```powershell
$content = [IO.File]::ReadAllText("path\to\file.ext")
# ... Regex Replace 등 작업 수행 ...
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText("path\to\file.ext", $content, $utf8NoBom)
```

이 가이드를 통해 파일 손상을 방지하고 완전한 UTF-8 무결성을 유지해야 합니다.
