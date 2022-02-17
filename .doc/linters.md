# Linter and Formatter (Prettier)

## Linter

The project use [Solhint](https://github.com/protofire/solhint) as linter for Solidity language that has its configuration in [./.solhint.json](./.solhint.json) file.

To run with node:

```sh
npm run solhint
```

## Formatter

[Prettier](https://github.com/prettier/prettier) is a fantastic tool that automatically formats the codebase according to a predefined style guide. Just agree on the rules beforehand at the team level, and then Prettier will then autoformat everyone’s code in the same way.

[Prettier-solidity](https://github.com/prettier-solidity/prettier-plugin-solidity) is a Prettier for solidity files that works hand-in-hand with Solhint. It helps to automatically fix many of the errors that Solhint finds, especially simple ones like indentation and code style.

Prettier is configured in [./.prettierrc](.prettierrc) file.

The project has installed as dependency [solhint-plugin-prettier](https://github.com/fvictorio/solhint-plugin-prettier), that allows Solhint to play nicely with Prettier-Solidity.

The is an script that yoyuu can run with npm:

```sh
npm run prettier:solidity
```

Take care that the command has --write flag will format and overwrite your existing files. As per the Prettier documentation, it’s a good idea to commit your code first.

## Git Hooks

In an ideal world, we’d always remember to run our linter and formatter before pushing code to our team’s codebase. Fortunately for us, we can automate this process with Git Hooks. To do that, we have [Husky](https://github.com/typicode/husky) as dev dependency in package.json. husky runs every time any of Us push to Github.