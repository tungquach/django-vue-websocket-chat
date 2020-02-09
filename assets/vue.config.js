module.exports = {
    publicPath: '/static/',
    pages: {
        index: 'src/pages/index.ts'
    },
    // disable hashes in filenames
    filenameHashing: false,
    // delete HTML related webpack plugins
    chainWebpack: config => {
      config.plugins.delete('html')
      config.plugins.delete('preload')
      config.plugins.delete('prefetch')
    },
    configureWebpack: {
        // No need for splitting
        optimization: {
          splitChunks: false
        }
    }
}