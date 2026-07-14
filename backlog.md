# Vibe CMS 랜딩페이지 이미지 작업 백로그

이 문서는 추후 진행할 시각 요소(이미지) 추가 및 레이아웃 개선 작업을 관리하기 위한 백로그 문서입니다. 사용자가 직접 전달할 이미지 샘플을 기반으로 작업을 수행할 예정입니다.

---

## 1. 관리자 화면 목업 이미지 배치 (AI Search 섹션)

*   **목적**: 방문자가 직접 질문을 클릭하여 테스트하는 "직접 체험해 보세요" 데모 영역에 관리자 관점의 실시간 모니터링 대시보드 화면을 함께 보여줌으로써 솔루션의 신뢰도와 완성도를 높임.
*   **위치**: `AI Search` 섹션 하단 `Interactive Chat Demo` 영역 (`.chat-demo-section`)
*   **작업 스펙**:
    *   **레이아웃 변경**: 기존 1열 배치에서 **좌/우 2컬럼 분할 레이아웃**으로 변경
        *   **좌측 컬럼**: 기존 대화형 채팅 데모 창 (`.chat-mockup`)
        *   **우측 컬럼**: 어두운 테마(Dark Mode)의 AI 관리자 모니터링 화면 프레임 및 이미지
    *   **적용할 이미지**: `assets/images/admin-mockup.png` (사용자 전달 예정)
    *   **추가 필요 CSS**:
        ```css
        .chat-demo-container {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 40px;
          max-width: 960px;
          margin: 0 auto;
          align-items: center;
        }
        .chat-admin-mockup {
          background: var(--bg-card);
          border: 1px solid var(--border-glass);
          border-radius: 16px;
          padding: 24px;
          display: flex;
          flex-direction: column;
          gap: 16px;
          box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        .chat-admin-header {
          font-size: 14px;
          font-weight: 600;
          color: var(--indigo-light);
          display: flex;
          align-items: center;
          gap: 8px;
        }
        .chat-admin-img {
          width: 100%;
          border-radius: 8px;
          border: 1px solid rgba(255, 255, 255, 0.05);
        }
        @media (max-width: 768px) {
          .chat-demo-container {
            grid-template-columns: 1fr;
            gap: 24px;
          }
        }
        ```

---

## 2. 공식 홈페이지 예시 이미지 배치 (Vibe CMS 섹션)

*   **목적**: "기획사 팬미팅 공지 작성"이라는 스토리텔링 시나리오에 현실감을 부여하기 위해, 실제 홈페이지에 포스팅된 공지사항 브라우저 화면을 보여줌.
*   **위치**: `Vibe CMS` 섹션 (`#vibe`) 내 엔터테인먼트 기획사 시나리오 비주얼 블록 (`.feature-block-visual` 내 `.story-flow`)
*   **작업 스펙**:
    *   **레이아웃 변경**: 기존 4단계 스토리 플로우 카드 상단에 액자 형태의 **미니 브라우저 목업** 추가
    *   **적용할 이미지**: `assets/images/event-mockup.png` (사용자 전달 예정)
    *   **추가 필요 CSS**:
        ```css
        .story-browser {
          background: rgba(255, 255, 255, 0.03);
          border: 1px solid var(--border-glass);
          border-radius: 12px;
          overflow: hidden;
          margin-bottom: 24px;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        .story-browser-header {
          background: rgba(255, 255, 255, 0.05);
          padding: 8px 12px;
          display: flex;
          align-items: center;
          gap: 6px;
          border-bottom: 1px solid var(--border-glass);
        }
        .story-browser-dot {
          width: 8px;
          height: 8px;
          border-radius: 50%;
          background: rgba(255, 255, 255, 0.2);
        }
        .story-browser-dot:nth-child(1) { background: #ff5f56; }
        .story-browser-dot:nth-child(2) { background: #ffbd2e; }
        .story-browser-dot:nth-child(3) { background: #27c93f; }
        .story-browser-title {
          margin-left: 10px;
          font-size: 11px;
          color: var(--text-secondary);
        }
        .story-browser-img {
          width: 100%;
          height: auto;
          display: block;
        }
        ```

---

## 3. 진행 대기 상태

1.  **샘플 이미지 수령**:
    *   `admin-mockup.png` (어드민 대시보드 캡처 또는 정밀 목업)
    *   `event-mockup.png` (공식 홈페이지 팬미팅 이벤트 공지글 캡처 또는 정밀 목업)
2.  **프로젝트 반영**:
    *   수령 후 `assets/images/` 경로에 파일 오버라이트 저장
    *   `index.html`, `ja/index.html` 내 구조 변경 마크업 릴리즈
    *   `style.css` 내 백로그 스타일 릴리즈
