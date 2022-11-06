module.exports = async (api) => {
  api.extendPackage({
    vue: {
      pluginOptions: {
        webpack: {
          dir: ['./webpack'],
        },
      },
    },
  })
}
