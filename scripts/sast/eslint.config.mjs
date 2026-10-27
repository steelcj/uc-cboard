// Security-only ESLint config used by scripts/sast/inside.sh.
// It is copied to the repo root inside the scan instance and is separate
// from the project's own .eslintrc, which it does not replace.
import security from 'eslint-plugin-security';
import noUnsanitized from 'eslint-plugin-no-unsanitized';
import tseslint from 'typescript-eslint';

// The source has eslint-disable comments for eslint-plugin-import rules.
// ESLint errors on disable comments for rules it cannot find, so this
// stub defines them as no-ops instead of installing the whole plugin.
const noop = { create: () => ({}) };
const importStub = { rules: { 'no-dynamic-require': noop } };

export default [
  {
    ignores: ['**/*.test.js', '**/__mocks__/**', 'eslint.config.mjs']
  },
  {
    files: ['**/*.{js,jsx,mjs,ts,tsx}'],
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: {
        ecmaFeatures: { jsx: true },
        sourceType: 'module'
      }
    },
    linterOptions: {
      // The project's own eslint-disable comments refer to rules this
      // config does not load.
      reportUnusedDisableDirectives: 'off'
    },
    plugins: {
      security,
      'no-unsanitized': noUnsanitized,
      import: importStub
    },
    rules: {
      ...security.configs.recommended.rules,
      ...noUnsanitized.configs.recommended.rules,
      // Flags almost every obj[key] access; too noisy to be useful here.
      'security/detect-object-injection': 'off',
      'no-eval': 'error',
      'no-implied-eval': 'error',
      'no-new-func': 'error'
    }
  }
];
