import os

def translate_file(src, dest, translations, is_index=True):
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply translations
    for ko_text, ja_text in translations.items():
        content = content.replace(ko_text, ja_text)

    # Update relative paths for subfolder
    content = content.replace('src="assets/', 'src="../assets/')
    
    # Update navigation links
    if is_index:
        content = content.replace('href="ai_strategy_proposal.html"', 'href="../ai_strategy_proposal.html"')
        content = content.replace('href="profile.html"', 'href="profile.html"')
    else:
        content = content.replace('href="index.html', 'href="index.html')
        content = content.replace('href="ai_strategy_proposal.html"', 'href="../ai_strategy_proposal.html"')

    # Update Language Switcher logic
    # In index.html: <a href="index.html" style="color: var(--text-primary);">KO</a>
    # In index.html: <a href="ja/index.html" style="color: var(--text-secondary)...
    
    if is_index:
        content = content.replace(
            '<a href="index.html" style="color: var(--text-primary);">KO</a>',
            '<a href="../index.html" style="color: var(--text-secondary); transition: color 0.3s;" onmouseover="this.style.color=\'var(--text-primary)\'" onmouseout="this.style.color=\'var(--text-secondary)\'">KO</a>'
        )
        content = content.replace(
            '<a href="ja/index.html" style="color: var(--text-secondary); transition: color 0.3s;" onmouseover="this.style.color=\'var(--text-primary)\'" onmouseout="this.style.color=\'var(--text-secondary)\'">JP</a>',
            '<a href="index.html" style="color: var(--text-primary);">JP</a>'
        )
    else:
        content = content.replace(
            '<a href="profile.html" style="color: var(--text-primary);">KO</a>',
            '<a href="../profile.html" style="color: var(--text-secondary); transition: color 0.3s;" onmouseover="this.style.color=\'var(--text-primary)\'" onmouseout="this.style.color=\'var(--text-secondary)\'">KO</a>'
        )
        content = content.replace(
            '<a href="ja/profile.html" style="color: var(--text-secondary); transition: color 0.3s;" onmouseover="this.style.color=\'var(--text-primary)\'" onmouseout="this.style.color=\'var(--text-secondary)\'">JP</a>',
            '<a href="profile.html" style="color: var(--text-primary);">JP</a>'
        )

    # Change lang attribute
    content = content.replace('<html lang="ko">', '<html lang="ja">')

    with open(dest, 'w', encoding='utf-8') as f:
        f.write(content)

index_translations = {
    # Meta / Title
    'JkSoft — Vibe Platform | 차세대 멀티테넌트 SaaS': 'JkSoft — Vibe Platform | 次世代マルチテナントSaaS',
    'JkSoft는 AI 최적화 기반의 멀티테넌트 SaaS 플랫폼 \'Vibe\'를 통해 디지털 비즈니스의 새로운 기준을 제시합니다.': 'JkSoftはAI最適化基盤のマルチテナントSaaSプラットフォーム「Vibe」を通じて、デジタルビジネスの新たな基準を提案します。',
    'AI 최적화 + 멀티테넌트 SaaS 플랫폼. 팬덤 관리부터 기업 홈페이지까지.': 'AI最適化＋マルチテナントSaaSプラットフォーム。ファンダム管理から企業サイトまで。',
    
    # Nav
    '제안서': '提案書',
    '문의하기': 'お問い合わせ',
    
    # Hero
    'SaaS Platform — Now Live': 'SaaS Platform — Now Live',
    '디지털 비즈니스의<br>\n        <span class="gradient-text">새로운 기준</span>을 만듭니다': 'デジタルビジネスの<br>\n        <span class="gradient-text">新たな基準</span>を創ります',
    'JkSoft는 AI 최적화(AIO) 기반의 멀티테넌트 SaaS 플랫폼 <strong>Vibe</strong>를 통해,<br>\n        팬덤 관리부터 기업 홈페이지까지 — 하나의 인프라로 모든 것을 실현합니다.': 'JkSoftはAI最適化(AIO)基盤のマルチテナントSaaSプラットフォーム<strong>Vibe</strong>を通じ、<br>\n        ファンダム管理から企業サイトまで、単一インフラですべてを実現します。',
    'Vibe 알아보기 →': 'Vibeの詳細を見る →',
    '📄 AI 전략 제안서 보기': '📄 AI戦略提案書を見る',
    
    # About
    '기술로 연결하고,<br>플랫폼으로 성장합니다': '技術で繋ぎ、<br>プラットフォームとして成長する',
    'JkSoft는 풀스택 SaaS 아키텍처 전문 소프트웨어 엔지니어링 팀입니다.\n            단순한 웹사이트 제작을 넘어, <strong>멀티테넌트 기반의 지능형 플랫폼</strong>을 설계하고 구축합니다.': 'JkSoftはフルスタックSaaSアーキテクチャ専門のソフトウェアエンジニアリングチームです。\n            単なるWeb制作を超え、<strong>マルチテナント基盤のインテリジェントプラットフォーム</strong>を設計・構築します。',
    '하나의 공유 인프라 위에서 다수의 고객사를 동시에 운영하면서도\n            데이터 격리와 브랜드 개인화를 완벽하게 보장하는 — 이것이 JkSoft가 추구하는 기술의 방향입니다.': '単一の共有インフラ上で複数の顧客企業を同時に運用しながらも、\n            データの分離とブランドのパーソナライズを完全に保証する。これがJkSoftの技術の方向性です。',
    '멀티테넌트 아키텍처': 'マルチテナント アーキテクチャ',
    'AI 최적화 기술': 'AI最適化技術',
    '다국어 지원 (한/영/중/일)': '多言語対応（韓/英/中/日）',
    '프론트 + 백엔드 풀스택': 'フロント＋バックエンド フルスタック',
    
    # Vibe
    '모든 비즈니스를 위한 단 하나의 플랫폼': 'あらゆるビジネスのための唯一のプラットフォーム',
    '팬덤, 아티스트, 솔루션, 에이전시 — 어떤 비즈니스 모델이든 Vibe 플랫폼 위에서 즉시 시작할 수 있습니다.': 'ファンダム、アーティスト、ソリューション、エージェンシー — あらゆるビジネスモデルがVibeプラットフォーム上で即座に開始できます。',
    '멀티테넌트 아키텍처': 'マルチテナント アーキテクチャ', # already translated, but as key
    '독립된 브랜드 파워': '独立したブランドパワー',
    '하나의 코어 시스템으로 수십 개의 브랜드를 동시 운영.\n            데이터는 안전하게 격리되고, 비용은 혁신적으로 절감됩니다.': '1つのコアシステムで数十のブランドを同時運用。\n            データは安全に分離され、コストは革新的に削減されます。',
    '화이트라벨링 (White-labeling)을 통해 테넌트마다\n            자신만의 테마, 로고, 도메인을 가질 수 있습니다.': 'ホワイトラベル（White-labeling）により、テナントごとに\n            独自のテーマ、ロゴ、ドメインを持つことができます。',
    '글로벌 다국어 지원': 'グローバル多言語対応',
    '4개 국어(한국어, 영어, 일본어, 중국어)를 네이티브하게 지원합니다.\n            URL 기반 i18n으로 검색 엔진에 최적화됩니다.': '4ヶ国語（韓国語、英語、日本語、中国語）をネイティブにサポート。\n            URLベースのi18nで検索エンジンに最適化されます。',
    
    # Tech Stack
    '최신 기술 스택의 집약체': '最新技術スタックの集大成',
    '성능, 확장성, 개발 생산성을 모두 만족하는 모던 테크 스택을 사용합니다.': 'パフォーマンス、拡張性、開発生産性をすべて満たすモダンテックスタックを採用しています。',
    'SSR 기반의 빠른 렌더링과 SEO 최적화': 'SSRベースの高速レンダ링とSEO最適化',
    '견고한 엔터프라이즈급 API 서버': '堅牢なエンタープライズ級APIサーバー',
    '타입 안정성으로 런타임 에러 최소화': '型安全性によるランタイムエラーの最小化',
    '성능과 안정성이 검증된 RDBMS': '性能と安定性が検証されたRDBMS',
    '데이터베이스 스키마 관리 및 마이그레이션': 'データベーススキーマの管理と移行',
    '컨테이너 기반 자원 격리와 무중단 배포': 'コンテナベースの隔離と無停止デプロイ',
    '초고속 CDN 및 안정적인 클라우드 엣지': '超高速CDNと安定したクラウドエッジ',
    '오픈소스 및 프라이빗 AI 모델 연동': 'OSSおよびプライベートAIモデル連携',
    
    # AIO
    'AI가 당신의 비즈니스를 최적화합니다': 'AIがあなたのビジネスを最適化します',
    '단순한 텍스트 생성을 넘어, SEO와 문맥에 맞게 콘텐츠를 구조화하는 AIO(AI Optimization) 기술을 탑재했습니다.': '単なるテキスト生成を超え、SEOと文脈に合わせてコンテンツを構造化するAIO(AI Optimization)技術を搭載しています。',
    '1. 초안 작성': '1. 原案の作成',
    '사람이 자연스러운 언어로 초안을 입력합니다.': '人が自然な言語で原案を入力します。',
    '2. 구조화 분석': '2. 構造化・分析',
    'AI 모델이 문맥을 분석하고 핵심 키워드를 추출합니다.': 'AIモデルが文脈を分析し、コアキーワードを抽出します。',
    '3. SEO 최적화 퍼블리싱': '3. SEO最適化パブリッシング',
    '검색 엔진이 좋아하는 HTML 태그와 시맨틱 구조로 자동 변환하여 배포합니다.': '検索エンジンが好むHTMLタグとセマンティック構造に自動変換してデプロイします。',
    'AIO 파이프라인의 이점': 'AIOパイプラインの利点',
    '기존의 SEO(검색엔진 최적화)는 사람이 직접 메타 태그를 작성하고 키워드를 배치해야 했습니다. JkSoft의 AIO 플랫폼은 이 모든 과정을 자동화합니다.': '従来のSEO（検索エンジン最適化）は、人が直接メタタグを作成しキーワードを配置する必要がありました。JkSoftのAIOプラットフォームは、このすべてのプロセスを自動化します。',
    'AI 검색 시대(ChatGPT, Gemini)에 특화된 시맨틱 데이터 구조': 'AI検索時代（ChatGPT, Gemini）に特化したセマンティックデータ構造',
    '마크다운(Markdown) 기반의 깔끔한 콘텐츠 관리': 'Markdownベースのクリーンなコンテンツ管理',
    '국가별(언어별) 검색어 트렌드 자동 반영': '国別・言語別の検索トレンドの自動反映',
    
    # Proposal CTA
    'AI 시대, 당신의 웹사이트는 보이지 않을 수 있습니다': 'AI時代、あなたのWebサイトは見えなくなるかもしれません',
    '제로 클릭(Zero-Click) 검색 시대가 도래했습니다. 트래픽에 의존하는 전통적 웹사이트는 AI의 답변 뒤로 사라집니다. JkSoft가 제안하는 생존 전략을 확인하세요.': 'ゼロクリック(Zero-Click)検索の時代が到来しました。トラフィックに依存する伝統的なWebサイトはAIの回答の裏に消えていきます。JkSoftが提案する生存戦略をご確認ください。',
    'AI 전략 제안서 읽어보기 →': 'AI戦略提案書を読む →',
    
    # Footer
    '기술로 연결하고, 플랫폼으로 성장합니다. 멀티테넌트 SaaS 기반의 차세대 디지털 솔루션.': '技術で繋ぎ、プラットフォームとして成長する。マルチテナントSaaS基盤の次世代デジタルソリューション。',
    '서비스': 'サービス',
    '자료': '資料',
    '연락처': '連絡先',
    'AI 전략 제안서': 'AI戦略提案書',
    '대표 프로필': '代表プロフィール',
    'Built with ♥ and TypeScript.': 'Built with ♥ and TypeScript.'
}

profile_translations = {
    # Meta
    '정형재 — JkSoft 대표 | Profile': 'Jeong Hyoung Jae — JkSoft 代表 | Profile',
    '20년 이상의 엔터프라이즈 시스템 분석·설계 경험과 풀스택 기술력. 대한항공, 삼성SDS, 현대그룹 등 대형 프로젝트 수행.': '20年以上のエンタープライズシステム要件定義・設計の経験とフルスタック技術。大韓航空、Samsung SDS、現代グループなど大型プロジェクトを遂行。',
    '정형재 — JkSoft 대표': 'Jeong Hyoung Jae — JkSoft 代表',
    '20년 이상의 엔터프라이즈 시스템 분석·설계 경험과 풀스택 기술력으로, 복잡한 비즈니스 요구를 기술로 실현하는 소프트웨어 엔지니어.': '20年以上のエンタープライズシステム要件定義・設計の経験とフルスタック技術で、複雑なビジネス要件を技術で実現するソフトウェアエンジニア。',
    
    # Navigation
    '제안서': '提案書',
    '문의하기': 'お問い合わせ',
    
    # Hero Profile
    '정형재 프로필': 'Jeong Hyoung Jae プロフィール',
    '정형재': 'Jeong Hyoung Jae',
    'JkSoft 대표': 'JkSoft 代表',
    '20년 이상의 엔터프라이즈 시스템 분석·설계 경험과 풀스택 기술력으로,<br>\n        복잡한 비즈니스 요구를 기술로 실현하는 소프트웨어 엔지니어': '20年以上のエンタープライズシステム要件定義・設計の経験とフルスタック技術で、<br>\n        複雑なビジネス要件を技術で実現するソフトウェアエンジニア',
    
    # Stats
    '엔터프라이즈 시스템 개발 경력': 'エンタープライズ システム開発経歴',
    '분석·설계·개발 프로젝트': '要件定義・設計・開発プロジェクト',
    '엔터프라이즈 고객사': 'エンタープライズ 顧客企業',
    'AA / PL / 분석 / 설계 / 개발': 'AA / PL / 要件定義 / 設計 / 開発',
    
    # Skills
    '핵심 기술 스택': 'コア技術スタック',
    '20년 이상의 프로젝트 경험에서 축적된 기술 역량입니다.\n          백엔드부터 프론트엔드, 인프라까지 풀스택 기술력을 보유하고 있습니다.': '20年以上のプロジェクト経験で蓄積された技術力です。\n          バックエンドからフロントエンド、インフラまでフルスタックの技術を保有しています。',
    '특화 영역': '特化領域',
    '멀티테넌트 SaaS': 'マルチテナント SaaS',
    '결제 시스템': '決済システム',
    '다국어/글로벌화': '多言語/グローバル化',
    '보안 (SSL/XSS/모의해킹)': 'セキュリティ (SSL/XSS/ペネトレーションテスト)',
    'AI 최적화 (AIO)': 'AI最適化 (AIO)',
    'AR/VR 헬스케어': 'AR/VR ヘルスケア',
    
    # Timeline
    '역할 성장 흐름': '役割と成長の道程',
    '개발자에서 아키텍트, 프로젝트 리더를 거쳐 SaaS 플랫폼 대표까지 —\n          기술과 함께 성장해 온 여정입니다.': '開発者からアーキテクト、プロジェクトリーダーを経てSaaSプラットフォーム代表へ —\n          技術と共に成長してきた軌跡です。',
    '현재': '現在',
    '헬스케어 AR/VR 플랫폼, 자동차 출입통제 SaaS, Vibe 멀티테넌트 플랫폼 개발.\n            AI 최적화(AIO) 기술 적용.': 'ヘルスケアAR/VRプラットフォーム、車両入退室管理SaaS、Vibeマルチテナントプラットフォーム開発。\n            AI最適化(AIO)技術の適用。',
    '풀스택 + 플랫폼': 'フルスタック + プラットフォーム',
    '삼성SDS Kubernetes 기반 플랫폼, 삼성서울병원 DW, Splunk/Elastic 데이터 분석 플랫폼.\n            다양한 기술 스택을 넘나드는 풀스택 역량 확장.': 'Samsung SDS Kubernetes基盤プラットフォーム、サムスンソウル病院DW、Splunk/Elasticデータ分析プラットフォーム。\n            多様な技術スタックを横断するフルスタック能力の拡張。',
    '설계 + 글로벌': '設計 + グローバル',
    '대한항공 2년 8개월 대형 프로젝트. 글로벌 결제 시스템(유니온페이, 알리페이, 카카오페이 등),\n            다국어 대응, 한국/미국 접근성(Accessibility) 설계.': '大韓航空2年8ヶ月の大型プロジェクト。グローバル決済システム（UnionPay、Alipay、KakaoPayなど）、\n            多言語対応、韓国・米国のアクセシビリティ（Accessibility）設計。',
    '현대그룹 5개 프로젝트 연속 수행. Application Architect 및 Project Leader 역할로\n            아키텍처 설계, DB 모델링, 보안 체계 구축을 주도.': '現代グループ5つのプロジェクトを連続遂行。Application ArchitectおよびProject Leaderとして\n            アーキテクチャ設計、DBモデリング、セキュリティ体系の構築を主導。',
    '개발자': '開発者',
    'Java/Spring 백엔드 중심 개발. 일본 시장 퍼블리싱 경험,\n            다수의 PG 결제 연동, CDN 인프라 구축 등 실전 경험 축적.': 'Java/Springバックエンド中心の開発。日本市場でのパブリッシング展開経験、\n            多数のPG決済連携、CDNインフラ構築などの実践経験を蓄積。',
    
    # Projects
    '주요 프로젝트': '主要プロジェクト',
    '엔터프라이즈급 시스템 분석·설계·개발을 주도한 대표적인 프로젝트들입니다.': 'エンタープライズ級システムの要件定義・設計・開発を主導した代表的なプロジェクトです。',
    '현재 진행 중': '現在進行中',
    '대표 / 기획 / 풀스택 개발': '代表 / 企画 / フルスタック開発',
    '멀티테넌트 SaaS 기반 팬덤 관리 플랫폼': 'マルチテナントSaaS基盤のファンダム管理プラットフォーム',
    'AI 콘텐츠 자동 최적화 (AIO)': 'AIコンテンツ自動最適化(AIO)',
    '4개 국어 지원 (한/영/중/일)': '4ヶ国語サポート（韓/英/日/中）',
    '화이트라벨링 및 테넌트별 브랜드 개인화': 'ホワイトラベルおよびテナント別ブランドパーソナライズ',
    '한화비전: 자동차 출입통제 / 아파트 커뮤니티': 'Hanwha Vision: 車両入退室管理 / マンションコミュニティ',
    '분석 / 설계 / 개발': '要件定義 / 設計 / 開発',
    '자동차 출입통제 시스템 개발': '車両入退室管理システムの開発',
    '아파트 커뮤니티 플랫폼': 'マンションコミュニティプラットフォーム',
    '마인드AI / FNI: 헬스케어 AR·VR 플랫폼': 'Mind AI / FNI: ヘルスケアAR・VRプラットフォーム',
    '분석 / 개발': '要件定義 / 開発',
    '<strong>바라봄</strong> — VR 인지장애 평가, 인지재활, 정서치료': '<strong>パラボム</strong> — VR認知障害評価、認知リハビリテーション、情動療法',
    '근골격계 질환 AR 운동치료 프로그램': '筋骨格系疾患向けAR運動治療プログラム',
    '<strong>Consurt</strong> — 정신건강 분석 프로젝트': '<strong>Consurt</strong> — メンタルヘルス分析プロジェクト',
    '개발': '開発',
    'Samsung SDS Fabrix 백엔드 개발': 'Samsung SDS Fabrix バックエンド開発',
    '테넌트별 Catalog 생성 및 관리': 'テナント別Catalogの生成および管理',
    'IDE Plugin 개발 (Eclipse, IntelliJ 대응)': 'IDE Plugin 開発（Eclipse、IntelliJ対応）',
    '프로젝트 산출물 자동 생성 및 관리': 'プロジェクト成果物の自動生成および管理',
    'Diagram, DAO/VO/SQL 자동 생성': 'Diagram、DAO/VO/SQL 自動生成',
    '경희의료원 사이트 개편': '慶熙医療院サイトリニューアル',
    '사이트 전면 개편 및 온라인 진료예약 기능 추가': 'サイトの全面リニューアルおよびオンライン診療予約機能の追加',
    '평화이즈 nU 연동': '平和イズnU連動',
    'Splunk / Elastic App 고도화': 'Splunk / Elastic App 高度化',
    'Splunk와 Elastic 플러그인 App 고도화': 'SplunkおよびElasticプラグインApp高度化',
    '데이터 분석 플랫폼 확장': 'データ分析プラットフォームの拡張',
    '삼성서울병원 DW 고도화': 'サムスンソウル病院 DWH 高度化',
    '환자/처방/수술 정보를 의사 연구개발 자료로 제공하는 데이터 웨어하우스 시스템': '患者/処方/手術情報を医師の研究開発資料として提供するデータウェアハウスシステム',
    '대한항공 사이트 개편': '大韓航空サイトリニューアル',
    '설계 / 개발': '設計 / 開発',
    '서비스 개발: 사전입국심사, 초과수하물, SNS 공유': 'サービス開発：事前入国審査、超過手荷物、SNS共有',
    '<strong>글로벌 결제</strong>: KICC, 유니온페이, 알리페이, 카카오페이, Yahoo Wallet, 일본 편의점': '<strong>グローバル決済</strong>：KICC、UnionPay、Alipay、KakaoPay、Yahoo Wallet、日本コンビニ決済',
    '한국/미국 접근성(Accessibility) 대응': '韓国・米国のアクセシビリティ（Accessibility）対応',
    '현대그룹 연속 프로젝트': '現代グループ連続プロジェクト',
    'Application Architect / Project Leader / 분석 / 설계 / 개발': 'Application Architect / Project Leader / 要件定義 / 設計 / 開発',
    '<strong>키즈현대</strong> — 어린이 교통안전 교육 사이트': '<strong>キッズ現代</strong> — 子供向け交通安全教育サイト',
    '<strong>현대자동차–기아 통합방송</strong> — Wowza 스트리밍 서비스': '<strong>現代自動車・起亜 統合放送</strong> — Wowzaストリーミングサービス',
    '<strong>현대제철</strong> 사이트 개편 — 다국어, 모바일 대응': '<strong>現代製鉄</strong> サイトリニューアル — 多言語、モバイル対応',
    '<strong>현대글로비스</strong> 지원시스템 통합 — 문서결재, SSO, 그룹웨어 연동': '<strong>現代グロービス</strong> 支援システム統合 — 電子決裁、SSO、グループウェア連動',
    '<strong>해비치호텔/해비치CC/롤링홀스</strong> — 호텔 예약 기간계 시스템 연동': '<strong>ヘビチホテル/ヘビチCC/ローリングヒルズ</strong> — ホテル予約基幹システム連動',
    '공통: DB 모델링, 보안(SSL/XSS/모의해킹), 다국어, 모바일': '共通：DBモデリング、セキュリティ（SSL/XSS/ペネトレーションテスト）、多言語、モバイル',
    '한국 방송사 컨텐츠 판매 (MBC / KBS)': '韓国放送局コンテンツ販売プラットフォーム（MBC / KBS）',
    '공통 / 분석 / 설계 / 개발': '共通 / 要件定義 / 設計 / 開発',
    '일본 시장 퍼블리싱: Yahoo Japan (OAuth 1.0), Rakuten (OpenID)': '日本市場でのパブリッシング展開：Yahoo Japan (OAuth 1.0), Rakuten (OpenID)',
    '다수 PG 연동: SPS, Digital Check, Yahoo Wallet, Rakuten': '多数のPG連携：SPS, Digital Check, Yahoo Wallet, Rakuten',
    'Groupon Japan, Edy 쿠폰 시스템': 'Groupon Japan、Edyクーポンシステム',
    '통계 시스템, SNS 연동 소셜댓글': '統計システム、SNS連動ソーシャルコメント',
    
    # Other Projects
    '기타 프로젝트': 'その他のプロジェクト',
    '전체 프로젝트 목록 보기 (9개)': '全プロジェクト一覧を見る（9件）',
    '프로젝트 목록 접기': 'プロジェクト一覧を閉じる',
    '해양수산부 기술거래소 개편': '海洋水産部 技術取引所 リニューアル',
    '오토앤 쇼핑몰 고도화 (현대/기아 멤버스)': 'Auto& ショッピングモール高度化（現代/起亜メンバーズ）',
    'CMS 서비스 고도화 (클라우드 솔루션)': 'CMSサービス高度化（クラウドソリューション）',
    'LG ESS 웹사이트 (6개 언어 지원)': 'LG ESS Webサイト（6ヶ国語サポート）',
    'SNC 콜센터 (증권담보대출)': 'SNCコールセンター（証券担保ローン）',
    'PL / 분석 / 설계 / 개발': 'PL / 要件定義 / 設計 / 開発',
    '한국단자 사이트 개편 (다국어/모바일)': '韓国端子サイトリニューアル（多言語/モバイル）',
    'AA / PL': 'AA / PL',
    'GS 통합고객관리시스템': 'GS 統合顧客管理システム',
    'CDN 서비스 (KINX / ESTsoft)': 'CDNサービス（KINX / ESTsoft）',
    'PuppyRed — 웹게임 플랫폼': 'PuppyRed — Webゲームプラットフォーム',
    
    # CTA
    '함께 프로젝트를 시작하고 싶으시다면': 'プロジェクトをご一緒に始めるなら',
    '20년 이상의 엔터프라이즈 경험을 바탕으로, 귀사의 비즈니스에 최적화된 기술 솔루션을 제안합니다.<br>\n          편하게 연락 주세요.': '20年以上のエンタープライズ経験をもとに、貴社のビジネスに最適な技術ソリューションを提案いたします。<br>\n          お気軽にお問い合わせください。',
    '📧 이메일 보내기': '📧 メールを送る',
    '📞 전화하기': '📞 電話をかける',
    '← 메인으로 돌아가기': '← メインへ戻る',
    
    # Footer
    '기술로 연결하고, 플랫폼으로 성장합니다. 멀티테넌트 SaaS 기반의 차세대 디지털 솔루션.': '技術で繋ぎ、プラットフォームとして成長する。マルチテナントSaaS基盤の次世代デジタルソリューション。',
    '서비스': 'サービス',
    '자료': '資料',
    '연락처': '連絡先',
    'AI 전략 제안서': 'AI戦略提案書',
    '대표 프로필': '代表プロフィール',
    'Built with ♥ and TypeScript.': 'Built with ♥ and TypeScript.'
}

# Run translation
translate_file("index.html", "ja/index.html", index_translations, is_index=True)
translate_file("profile.html", "ja/profile.html", profile_translations, is_index=False)

print("Translation completed")
