# Setup

## Yarn
```
brew install yarn
cd app/
yarn init -y
```

## Webpack, Babel
```
yarn add --dev webpack babel-core babel-loader@7 babel-preset-react babel-preset-es2015 node-sass css-loader sass-loader style-loader
```

## React
```
yarn add react react-dom
```

## Dev Server
```
yarn add --dev webpack-cli webpack-dev-server html-webpack-plugin
```

## Docker
```
docker build -t <REGISTRY>/<REPOSITORY>:<TAG>
docker run -p 80:80 <REGISTRY>/<REPOSITORY>:<TAG>
```
