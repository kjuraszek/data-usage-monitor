module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  collectCoverage: true,
  collectCoverageFrom: ["**/*.{js,vue}", "!**/node_modules/**", "!**.config.js", "!**/coverage/**", "!**/dist/**"],
  setupFilesAfterEnv: ['<rootDir>/tests/unit/setup.js']
}
