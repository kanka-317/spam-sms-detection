document.addEventListener('DOMContentLoaded', () => {
  const darkModeBtn = document.getElementById('darkModeToggle');
  const clearBtn = document.getElementById('clearText');
  const textarea = document.querySelector('textarea');
  const wordCount = document.getElementById('wordCount');

  // 🌙 Toggle Dark Mode
  if (darkModeBtn) {
    darkModeBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      darkModeBtn.textContent = document.body.classList.contains('dark-mode')
        ? '☀️ Light Mode'
        : '🌙 Dark Mode';
    });
  }

  // 🧹 Clear Text
  if (clearBtn && textarea && wordCount) {
    clearBtn.addEventListener('click', () => {
      textarea.value = '';
      wordCount.textContent = 'Words: 0, Characters: 0';
    });

    // Count
    textarea.addEventListener('input', () => {
      const text = textarea.value.trim();
      const words = text === '' ? 0 : text.split(/\s+/).length;
      const chars = text.length;
      wordCount.textContent = `Words: ${words}, Characters: ${chars}`;
    });
  }
});
