```bash
python3 build-release.py --tag 1.39.0
[BUILD] resolving upstream tag '1.39.0'...
[BUILD] tag '1.39.0' -> commit 7b8969fe81f3198be695d9f1717ba755e574a676
[BUILD] cloning at pinned commit...
Cloning into 'scratch-cboard'...
remote: Enumerating objects: 46287, done.
remote: Counting objects: 100% (3009/3009), done.
remote: Compressing objects: 100% (705/705), done.
remote: Total 46287 (delta 2716), reused 2306 (delta 2304), pack-reused 43278 (from 2)
Receiving objects: 100% (46287/46287), 229.94 MiB | 1.95 MiB/s, done.
Resolving deltas: 100% (32055/32055), done.
Note: switching to '7b8969fe81f3198be695d9f1717ba755e574a676'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 7b8969fe Improves unlock button click reliability
[BUILD] installing (--ignore-scripts) and building...
yarn install v1.22.22
[1/4] Resolving packages...
[2/4] Fetching packages...
warning bare-fs@4.5.5: The engine "bare" appears to be invalid.
warning bare-os@3.7.0: The engine "bare" appears to be invalid.
[3/4] Linking dependencies...
warning " > @microsoft/applicationinsights-web@2.8.18" has unmet peer dependency "tslib@*".
warning "@microsoft/applicationinsights-web > @microsoft/applicationinsights-analytics-js@2.8.18" has unmet peer dependency "tslib@*".
warning "@microsoft/applicationinsights-web > @microsoft/applicationinsights-channel-js@2.8.18" has unmet peer dependency "tslib@*".
warning "@microsoft/applicationinsights-web > @microsoft/applicationinsights-common@2.8.18" has unmet peer dependency "tslib@*".
warning "@microsoft/applicationinsights-web > @microsoft/applicationinsights-core-js@2.8.18" has unmet peer dependency "tslib@*".
warning "@microsoft/applicationinsights-web > @microsoft/applicationinsights-dependencies-js@2.8.18" has unmet peer dependency "tslib@*".
warning "@microsoft/applicationinsights-web > @microsoft/applicationinsights-properties-js@2.8.18" has unmet peer dependency "tslib@*".
warning "formik > create-react-context@0.2.3" has incorrect peer dependency "react@^0.14.0 || ^15.0.0 || ^16.0.0".
warning " > react-intl@2.9.0" has incorrect peer dependency "react@^0.14.9 || ^15.0.0 || ^16.0.0".
warning " > react-redux@5.1.2" has incorrect peer dependency "react@^0.14.0 || ^15.0.0-0 || ^16.0.0-0".
warning " > react-share@2.4.0" has incorrect peer dependency "react@^0.13.0 || ^0.14.0 || ^15.0.0 || ^16.0.0-0".
warning " > @babel/plugin-proposal-private-property-in-object@7.21.11" has unmet peer dependency "@babel/core@^7.0.0-0".
warning "@babel/plugin-proposal-private-property-in-object > @babel/helper-create-class-features-plugin@7.28.6" has unmet peer dependency "@babel/core@^7.0.0".
warning "@babel/plugin-proposal-private-property-in-object > @babel/plugin-syntax-private-property-in-object@7.14.5" has unmet peer dependency "@babel/core@^7.0.0-0".
warning "@babel/plugin-proposal-private-property-in-object > @babel/helper-create-class-features-plugin > @babel/helper-replace-supers@7.28.6" has unmet peer dependency "@babel/core@^7.0.0".
warning "@craco/craco > autoprefixer@10.4.27" has unmet peer dependency "postcss@^8.1.0".
warning "@craco/craco > cosmiconfig-typescript-loader@1.0.9" has unmet peer dependency "@types/node@*".
warning "@craco/craco > cosmiconfig-typescript-loader > ts-node@10.9.2" has unmet peer dependency "@types/node@*".
warning " > babel-plugin-transform-import-meta@2.3.3" has unmet peer dependency "@babel/core@^7.10.0".
warning " > node-polyfill-webpack-plugin@2.0.1" has unmet peer dependency "webpack@>=5".
warning "react-scripts > eslint-config-react-app > eslint-plugin-flowtype@8.0.3" has unmet peer dependency "@babel/plugin-syntax-flow@^7.14.5".
warning "react-scripts > eslint-config-react-app > eslint-plugin-flowtype@8.0.3" has unmet peer dependency "@babel/plugin-transform-react-jsx@^7.14.9".
warning " > ts-loader@9.5.4" has unmet peer dependency "webpack@^5.0.0".
[4/4] Building fresh packages...
warning Ignored scripts due to flag.
Done in 99.78s.
yarn run v1.22.22
$ craco build  --verbose && sw-precache --config=sw-precache-config.js
Project root path resolved to:  /home/initial/2-areas/development/uc-cboard/scratch-cboard
Override started with arguments:  [
  '/home/initial/.nvm/versions/node/v22.14.0/bin/node',
  '/home/initial/2-areas/development/uc-cboard/scratch-cboard/node_modules/@craco/craco/dist/scripts/build.js',
  '--verbose'
]
For environment:  production
Config file path resolved to:  /home/initial/2-areas/development/uc-cboard/scratch-cboard/craco.config.js
Applied craco config plugins.
Found Webpack prod config at:  /home/initial/2-areas/development/uc-cboard/scratch-cboard/node_modules/react-scripts/config/webpack.config.js
Added Babel plugins.
Added Babel plugins.
Overrided ESLint config to enable an ignore file.
Overrided PostCSS loader.
Overrided PostCSS loader.
Overrided PostCSS loader.
Overrided PostCSS loader.
Added webpack plugins.
Merged webpack config with 'webpack.configure'.
Applied webpack config plugins.
Overrode require cache for module: /home/initial/2-areas/development/uc-cboard/scratch-cboard/node_modules/react-scripts/config/webpack.config.js
Overrode Webpack prod config.
Building CRA at:  /home/initial/2-areas/development/uc-cboard/scratch-cboard/node_modules/react-scripts/scripts/build.js
Creating an optimized production build...
Browserslist: browsers data (caniuse-lite) is 6 months old. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
Browserslist: browsers data (caniuse-lite) is 6 months old. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
Compiled successfully.

File sizes after gzip:

  1.5 MB     build/static/js/main.b05cc009.js
  794.11 kB  build/static/js/217.da5a8789.chunk.js
  731.81 kB  build/static/js/7664.221a51ef.chunk.js
  72.86 kB   build/static/js/7879.f352ef69.chunk.js
  71.26 kB   build/static/js/5267.43833f49.chunk.js
  70.81 kB   build/static/js/169.149aad41.chunk.js
  70.3 kB    build/static/js/8971.d14afc47.chunk.js
  70.2 kB    build/static/js/3609.65132fcf.chunk.js
  70.1 kB    build/static/js/8427.57a39a96.chunk.js
  69.58 kB   build/static/js/3919.614c19c9.chunk.js
  69.19 kB   build/static/js/3714.d96854e8.chunk.js
  68.96 kB   build/static/js/311.ad53f456.chunk.js
  68.86 kB   build/static/js/3607.417db4dd.chunk.js
  68.72 kB   build/static/js/5923.e8f19367.chunk.js
  68.58 kB   build/static/js/1676.4ad5ebc0.chunk.js
  68.56 kB   build/static/js/2565.df9e1252.chunk.js
  68.15 kB   build/static/js/4771.90aad768.chunk.js
  67.96 kB   build/static/js/6377.d632d7b1.chunk.js
  67.53 kB   build/static/js/3861.babe27cc.chunk.js
  67.47 kB   build/static/js/9727.7c99dfa9.chunk.js
  66.34 kB   build/static/js/8345.d29c8a9c.chunk.js
  66.16 kB   build/static/js/4420.b6ab0f1a.chunk.js
  65.67 kB   build/static/js/756.5db1ffa6.chunk.js
  65.46 kB   build/static/js/277.3b7bb7a9.chunk.js
  65.16 kB   build/static/js/5161.542f319e.chunk.js
  64.4 kB    build/static/js/9505.ae0872b7.chunk.js
  64.29 kB   build/static/js/533.0390169b.chunk.js
  63 kB      build/static/js/2200.2a8e8cdc.chunk.js
  62.76 kB   build/static/js/9010.6005f64e.chunk.js
  60.2 kB    build/static/js/4138.5fceaeea.chunk.js
  58.3 kB    build/static/js/5673.e65f85b0.chunk.js
  57.81 kB   build/static/js/9174.37f3cc51.chunk.js
  57.58 kB   build/static/js/8710.7c26ca42.chunk.js
  56.78 kB   build/static/js/7251.2189add3.chunk.js
  56.7 kB    build/static/js/5841.f4635a5d.chunk.js
  56.11 kB   build/static/js/6869.9aa7c98a.chunk.js
  55.86 kB   build/static/js/5211.168a086c.chunk.js
  55.75 kB   build/static/js/3425.134971d8.chunk.js
  55.62 kB   build/static/js/7815.27ab66d5.chunk.js
  55.35 kB   build/static/js/1605.487b0231.chunk.js
  55.2 kB    build/static/js/2417.2da0fdb2.chunk.js
  54.94 kB   build/static/js/7733.5278d498.chunk.js
  54.93 kB   build/static/js/1821.ce833afe.chunk.js
  54.7 kB    build/static/js/3637.df90a115.chunk.js
  54.65 kB   build/static/js/1640.c839f5c4.chunk.js
  54.6 kB    build/static/js/9616.2baff470.chunk.js
  54.57 kB   build/static/js/2769.7db15cda.chunk.js
  54.41 kB   build/static/js/2581.b1cee9eb.chunk.js
  54.38 kB   build/static/js/1345.55b6846f.chunk.js
  54.36 kB   build/static/js/8561.da481280.chunk.js
  54.21 kB   build/static/js/8389.5aa0dcf9.chunk.js
  54.1 kB    build/static/js/8219.02757564.chunk.js
  54.04 kB   build/static/js/3085.68c143f0.chunk.js
  53.96 kB   build/static/js/9699.61d4de48.chunk.js
  53.69 kB   build/static/js/8555.ce78ef15.chunk.js
  52.97 kB   build/static/js/6330.06c747bc.chunk.js
  52.71 kB   build/static/js/3593.c3db869e.chunk.js
  52.41 kB   build/static/js/7277.6ed5977b.chunk.js
  52.28 kB   build/static/js/4387.44cdb009.chunk.js
  52.06 kB   build/static/js/7982.f6cc63c5.chunk.js
  51.89 kB   build/static/js/4011.b4efad6d.chunk.js
  51.59 kB   build/static/js/1715.b4a195c6.chunk.js
  51.16 kB   build/static/js/6516.c7281bb0.chunk.js
  50.41 kB   build/static/js/4679.dda5f549.chunk.js
  46.71 kB   build/static/js/1885.9643c787.chunk.js
  46.7 kB    build/static/js/9832.ebe035aa.chunk.js
  46.69 kB   build/static/js/518.f1796302.chunk.js
  46.69 kB   build/static/js/4388.322907ec.chunk.js
  46.69 kB   build/static/js/6550.79277405.chunk.js
  46.69 kB   build/static/js/7510.c190919a.chunk.js
  46.69 kB   build/static/js/3572.9be2d29d.chunk.js
  37.89 kB   build/static/js/1610.4b28c88e.chunk.js
  13.41 kB   build/static/css/main.d7b118b8.css
  2.34 kB    build/static/js/6485.d8d3f94b.chunk.js

The bundle size is significantly larger than recommended.
Consider reducing it with code splitting: https://goo.gl/9VhYWB
You can also analyze the project dependencies: https://goo.gl/LeUzfb

The project was built assuming it is hosted at /.
You can control this with the homepage field in your package.json.

The build folder is ready to be deployed.
You may serve it with a static server:

  yarn global add serve
  serve -s build

Find out more about deployment here:

  https://cra.link/deployment

build//symbols/mulberry/correct.svg
build//symbols/mulberry/no.svg
build//symbols/cboard/speech_bubble.svg
build//symbols/mulberry/clock.svg
build//symbols/mulberry/food.svg
build//symbols/mulberry/drinks.svg
build//symbols/mulberry/jelly_beans.svg
build//symbols/cboard/activities.svg
build//symbols/cboard/emotions.svg
build//symbols/mulberry/body_outline.svg
build//symbols/mulberry/generic_clothes.svg
build//symbols/cboard/people.svg
build//symbols/mulberry/shapesorter.svg
build//symbols/cboard/kitchen_items.svg
build//symbols/mulberry/school.svg
build//symbols/cboard/animals.svg
build//symbols/mulberry/technology.svg
build//symbols/cboard/weather.svg
build//symbols/cboard/plants.svg
build//symbols/cboard/sports.svg
build//symbols/mulberry/travel.svg
build//symbols/mulberry/globe.svg
build//symbols/cboard/position.svg
build//symbols/mulberry/toys.svg
build//symbols/cboard/actions.svg
build//symbols/mulberry/ask_,_to.svg
build//symbols/mulberry/furniture.svg
build//symbols/cboard/personal_hygiene.svg
build//symbols/mulberry/count_,_to.svg
build//symbols/mulberry/hello.svg
build//symbols/arasaac/goodbye.png
build//symbols/mulberry/good.svg
build//symbols/mulberry/bad.svg
build//symbols/mulberry/non_speaking.svg
build//symbols/arasaac/thanks.png
build//symbols/arasaac/please.png
build//symbols/mulberry/hungry.svg
build//symbols/mulberry/want_,_to.svg
build//symbols/arasaac/ampersand.png
build//symbols/mulberry/soup.svg
build//symbols/mulberry/vegetables.svg
build//symbols/mulberry/fruit.svg
build//symbols/mulberry/pizza_2.svg
build//symbols/mulberry/bread.svg
build//symbols/mulberry/boiled_egg.svg
build//symbols/mulberry/fried_egg.svg
build//symbols/mulberry/croissant.svg
build//symbols/mulberry/cereal.svg
build//symbols/mulberry/porridge.svg
build//symbols/mulberry/pancakes.svg
build//symbols/mulberry/pasta.svg
build//symbols/mulberry/poultry.svg
build//symbols/mulberry/beef.svg
build//symbols/mulberry/fish.svg
build//symbols/mulberry/spaghetti_bolognaise.svg
build//symbols/mulberry/hamburger.svg
build//symbols/mulberry/hot_dog.svg
build//symbols/mulberry/pie.svg
build//symbols/mulberry/pepper_mill.svg
build//symbols/mulberry/salt.svg
build//symbols/mulberry/tomato_sauce.svg
build//symbols/mulberry/vinegar.svg
build//symbols/mulberry/sandwich.svg
build//symbols/mulberry/bagel_2.svg
build//symbols/mulberry/toast.svg
build//symbols/mulberry/cheese.svg
build//symbols/mulberry/noodles.svg
build//symbols/mulberry/chips.svg
build//symbols/mulberry/salad.svg
build//symbols/mulberry/potato.svg
build//symbols/mulberry/mash_potato_1.svg
build//symbols/mulberry/sweet_potato.svg
build//symbols/mulberry/rice.svg
build//symbols/mulberry/baked_beans_2.svg
build//symbols/mulberry/sweetcorn.svg
build//symbols/mulberry/beetroot.svg
build//symbols/mulberry/carrot.svg
build//symbols/mulberry/tomato.svg
build//symbols/mulberry/cucumber.svg
build//symbols/mulberry/cabbage.svg
build//symbols/mulberry/onion.svg
build//symbols/mulberry/spring_onions.svg
build//symbols/mulberry/pepper.svg
build//symbols/mulberry/chilli_pepper.svg
build//symbols/mulberry/lettuce.svg
build//symbols/mulberry/asparagus.svg
build//symbols/mulberry/radish.svg
build//symbols/mulberry/aubergine.svg
build//symbols/mulberry/broccoli.svg
build//symbols/mulberry/peas.svg
build//symbols/mulberry/avocado.svg
build//symbols/mulberry/green_beans.svg
build//symbols/mulberry/spinach.svg
build//symbols/mulberry/pumpkin.svg
build//symbols/mulberry/brussel_sprouts.svg
build//symbols/mulberry/thirsty.svg
build//symbols/mulberry/drink.svg
build//symbols/mulberry/water.svg
build//symbols/mulberry/orange_juice.svg
build//symbols/mulberry/apple_juice.svg
build//symbols/mulberry/grape_juice.svg
build//symbols/mulberry/cranberry_juice.svg
build//symbols/mulberry/pineapple_juice.svg
build//symbols/mulberry/lemonade.svg
build//symbols/mulberry/milk.svg
build//symbols/mulberry/milkshake.svg
build//symbols/mulberry/hot_chocolate.svg
build//symbols/mulberry/tea.svg
build//symbols/mulberry/coffee.svg
build//symbols/mulberry/wine.svg
build//symbols/mulberry/beer.svg
build//symbols/mulberry/straw.svg
build//symbols/mulberry/carrot_soup.svg
build//symbols/mulberry/chicken_soup.svg
build//symbols/mulberry/mushroom_soup.svg
build//symbols/mulberry/onion_soup.svg
build//symbols/mulberry/pea_soup.svg
build//symbols/mulberry/tomato_soup.svg
build//symbols/mulberry/vegetable_soup.svg
build//symbols/mulberry/ice_cream.svg
build//symbols/mulberry/chocolate.svg
build//symbols/mulberry/crisps.svg
build//symbols/mulberry/marshmallows.svg
build//symbols/mulberry/biscuits.svg
build//symbols/mulberry/candy_cane.svg
build//symbols/mulberry/nuts.svg
build//symbols/mulberry/cake_slice_2.svg
build//symbols/mulberry/chocolate_chip_biscuit.svg
build//symbols/mulberry/yogurt.svg
build//symbols/mulberry/ice_lolly.svg
build//symbols/mulberry/pretzel.svg
build//symbols/mulberry/peanut.svg
build//symbols/mulberry/strawberry.svg
build//symbols/mulberry/apple.svg
build//symbols/mulberry/apricot.svg
build//symbols/mulberry/peach.svg
build//symbols/mulberry/mango.svg
build//symbols/mulberry/pear.svg
build//symbols/mulberry/orange.svg
build//symbols/mulberry/melon.svg
build//symbols/mulberry/banana.svg
build//symbols/mulberry/kiwi.svg
build//symbols/mulberry/pineapple.svg
build//symbols/mulberry/watermelon.svg
build//symbols/mulberry/cherry.svg
build//symbols/mulberry/grapefruit.svg
build//symbols/mulberry/grapes.svg
build//symbols/arasaac/i_am.png
build//symbols/arasaac/you_are.png
build//symbols/arasaac/are_you.png
build//symbols/mulberry/happy_man.svg
build//symbols/mulberry/sad_man.svg
build//symbols/mulberry/angry_man.svg
build//symbols/mulberry/afraid_man.svg
build//symbols/mulberry/confused_man.svg
build//symbols/mulberry/hot_person.svg
build//symbols/mulberry/excited_man.svg
build//symbols/mulberry/relax_3_,_to.svg
build//symbols/cboard/clothing_accessories.svg
build//symbols/mulberry/shirt.svg
build//symbols/mulberry/t-shirt.svg
build//symbols/mulberry/trousers.svg
build//symbols/mulberry/shorts.svg
build//symbols/mulberry/jacket.svg
build//symbols/mulberry/coat.svg
build//symbols/mulberry/blouse.svg
build//symbols/mulberry/dress.svg
build//symbols/mulberry/jumper.svg
build//symbols/mulberry/hoodie.svg
build//symbols/mulberry/skirt.svg
build//symbols/mulberry/vest.svg
build//symbols/mulberry/pyjamas.svg
build//symbols/mulberry/artist_palette.svg
build//symbols/mulberry/glasses.svg
build//symbols/mulberry/sunglasses.svg
build//symbols/mulberry/bobble_hat.svg
build//symbols/mulberry/cap.svg
build//symbols/mulberry/bow_tie.svg
build//symbols/mulberry/tie.svg
build//symbols/mulberry/socks.svg
build//symbols/mulberry/gloves.svg
build//symbols/mulberry/boots.svg
build//symbols/mulberry/bra.svg
build//symbols/mulberry/boxer_shorts.svg
build//symbols/mulberry/pants.svg
build//symbols/mulberry/purse.svg
build//symbols/mulberry/jewellery.svg
build//symbols/mulberry/sandals.svg
build//symbols/mulberry/trainers.svg
build//symbols/mulberry/scarf.svg
build//symbols/mulberry/umbrella.svg
build//symbols/mulberry/watch.svg
build//symbols/arasaac/i_am_pain.png
build//symbols/mulberry/itch.svg
build//symbols/mulberry/head.svg
build//symbols/mulberry/neutral_face.svg
build//symbols/mulberry/neck.svg
build//symbols/mulberry/shoulder.svg
build//symbols/mulberry/arms.svg
build//symbols/mulberry/right_hand.svg
build//symbols/mulberry/left_hand.svg
build//symbols/mulberry/elbow.svg
build//symbols/mulberry/back.svg
build//symbols/mulberry/stomach_1.svg
build//symbols/mulberry/finger.svg
build//symbols/mulberry/leg.svg
build//symbols/mulberry/foot.svg
build//symbols/mulberry/throat.svg
build//symbols/mulberry/hip.svg
build//symbols/mulberry/bottom_3.svg
build//symbols/mulberry/first_aid_box.svg
build//symbols/mulberry/thumb.svg
build//symbols/mulberry/toe_nail.svg
build//symbols/mulberry/fingernail.svg
build//symbols/mulberry/muscles.svg
build//symbols/mulberry/skin.svg
build//symbols/mulberry/bone_2.svg
build//symbols/mulberry/knee.svg
build//symbols/mulberry/eyebrow.svg
build//symbols/mulberry/eyes.svg
build//symbols/mulberry/eye.svg
build//symbols/mulberry/eyelash.svg
build//symbols/mulberry/cheek.svg
build//symbols/mulberry/ear.svg
build//symbols/mulberry/lips_1.svg
build//symbols/mulberry/teeth.svg
build//symbols/mulberry/gum.svg
build//symbols/mulberry/tongue.svg
build//symbols/mulberry/chin.svg
build//symbols/mulberry/now.svg
build//symbols/mulberry/yesterday.svg
build//symbols/mulberry/today.svg
build//symbols/mulberry/tomorrow.svg
build//symbols/mulberry/morning.svg
build//symbols/mulberry/afternoon.svg
build//symbols/mulberry/night.svg
build//symbols/mulberry/day.svg
build//symbols/mulberry/this_week.svg
build//symbols/mulberry/weekend.svg
build//symbols/mulberry/next_week.svg
build//symbols/mulberry/this_month.svg
build//symbols/mulberry/next_month.svg
build//symbols/mulberry/last_month.svg
build//symbols/mulberry/one_hour.svg
build//symbols/mulberry/minute.svg
build//symbols/mulberry/second.svg
build//symbols/arasaac/i_have.png
build//symbols/arasaac/i_saw.png
build//symbols/mulberry/dog.svg
build//symbols/mulberry/cat.svg
build//symbols/mulberry/hamster.svg
build//symbols/mulberry/rabbit.svg
build//symbols/mulberry/hedgehog.svg
build//symbols/mulberry/horse.svg
build//symbols/mulberry/donkey.svg
build//symbols/mulberry/toad.svg
build//symbols/mulberry/sheep.svg
build//symbols/mulberry/dog_kennel.svg
build//symbols/mulberry/cage.svg
build//symbols/mulberry/stable.svg
build//symbols/mulberry/frog.svg
build//symbols/mulberry/chick.svg
build//symbols/mulberry/live_chicken.svg
build//symbols/mulberry/mouse.svg
build//symbols/mulberry/rat.svg
build//symbols/mulberry/parrot.svg
build//symbols/mulberry/nest.svg
build//symbols/mulberry/goose.svg
build//symbols/mulberry/cow.svg
build//symbols/cboard/wild_animals.svg
build//symbols/cboard/marine_animals.svg
build//symbols/cboard/insects.svg
build//symbols/cboard/birds.svg
build//symbols/mulberry/tortoise.svg
build//symbols/mulberry/camel.svg
build//symbols/mulberry/piglet.svg
build//symbols/mulberry/black.svg
build//symbols/mulberry/white.svg
build//symbols/mulberry/mauve.svg
build//symbols/mulberry/yellow.svg
build//symbols/mulberry/pink.svg
build//symbols/mulberry/blue.svg
build//symbols/mulberry/green.svg
build//symbols/mulberry/red.svg
build//symbols/mulberry/colour.svg
build//symbols/mulberry/zero.svg
build//symbols/mulberry/one.svg
build//symbols/mulberry/two.svg
build//symbols/mulberry/three.svg
build//symbols/mulberry/four.svg
build//symbols/mulberry/five.svg
build//symbols/mulberry/six.svg
build//symbols/mulberry/seven.svg
build//symbols/mulberry/eight.svg
build//symbols/mulberry/nine.svg
build//symbols/mulberry/circle.svg
build//symbols/mulberry/oval.svg
build//symbols/mulberry/triangle_equilateral.svg
build//symbols/mulberry/square.svg
build//symbols/mulberry/rectangle.svg
build//symbols/mulberry/pentagon.svg
build//symbols/mulberry/hexagon.svg
build//symbols/mulberry/octagon.svg
build//symbols/mulberry/star_2.svg
build//symbols/mulberry/diamond.svg
build//symbols/mulberry/pyramid_triangular_base.svg
build//symbols/mulberry/cycle_,_to.svg
build//symbols/mulberry/basketball.svg
build//symbols/mulberry/bowler_1.svg
build//symbols/mulberry/computer_game.svg
build//symbols/mulberry/flatscreen_tv.svg
build//symbols/mulberry/jigsaw_puzzle.svg
build//symbols/mulberry/kick_ball_1_,_to.svg
build//symbols/mulberry/bingo.svg
build//symbols/mulberry/bathe_,_to.svg
build//symbols/mulberry/work_,_to.svg
build//symbols/mulberry/cook_,_to.svg
build//symbols/mulberry/exercise_,_to.svg
build//symbols/mulberry/run_,_to.svg
build//symbols/mulberry/armwrestle_,_to.svg
build//symbols/mulberry/celebrate_3_,_to.svg
build//symbols/mulberry/swim_,_to.svg
build//symbols/mulberry/fish_,_to.svg
build//symbols/mulberry/darts.svg
build//symbols/mulberry/playing_cards.svg
build//symbols/mulberry/pen.svg
build//symbols/mulberry/pencil.svg
build//symbols/mulberry/pencil_sharpener.svg
build//symbols/mulberry/pencil_case.svg
build//symbols/mulberry/school_bag.svg
build//symbols/mulberry/notebook.svg
build//symbols/mulberry/ring_binder.svg
build//symbols/mulberry/calculator.svg
build//symbols/mulberry/scissors.svg
build//symbols/mulberry/blackboard.svg
build//symbols/mulberry/teacher_2a.svg
build//symbols/mulberry/class_room.svg
build//symbols/mulberry/tippex.svg
build//symbols/mulberry/crayon.svg
build//symbols/mulberry/glue.svg
build//symbols/mulberry/stapler.svg
build//symbols/mulberry/algebra_class.svg
build//symbols/mulberry/art_class.svg
build//symbols/mulberry/drama_class.svg
build//symbols/mulberry/english_class.svg
build//symbols/mulberry/geography_class.svg
build//symbols/mulberry/history_class.svg
build//symbols/mulberry/maths_class.svg
build//symbols/mulberry/it_class.svg
build//symbols/mulberry/music_class.svg
build//symbols/mulberry/science_class.svg
build//symbols/mulberry/no_class.svg
build//symbols/mulberry/family.svg
build//symbols/arasaac/characters.png
build//symbols/mulberry/dad.svg
build//symbols/mulberry/mum.svg
build//symbols/mulberry/teacher_1b.svg
build//symbols/mulberry/doctor_1a.svg
build//symbols/mulberry/nurse_2a.svg
build//symbols/mulberry/speech_language_therapist_1b.svg
build//symbols/mulberry/police_1b.svg
build//symbols/mulberry/delivery_person_1a.svg
build//symbols/mulberry/post_person_1a.svg
build//symbols/mulberry/dentist_1a.svg
build//symbols/mulberry/carpenter_1b.svg
build//symbols/mulberry/secretary_1a.svg
build//symbols/mulberry/taxi_driver_1c.svg
build//symbols/mulberry/gardener_2b.svg
build//symbols/mulberry/it_assistant_2b.svg
build//symbols/mulberry/get_,_to.svg
build//symbols/mulberry/give_,_to.svg
build//symbols/mulberry/put_,_to.svg
build//symbols/mulberry/hear_,_to.svg
build//symbols/mulberry/come_,_to.svg
build//symbols/mulberry/go_,_to.svg
build//symbols/mulberry/wait_,_to.svg
build//symbols/mulberry/take_,_to.svg
build//symbols/mulberry/watch_,_to.svg
build//symbols/mulberry/think_,_to.svg
build//symbols/mulberry/make_,_to.svg
build//symbols/mulberry/break_2_,_to.svg
build//symbols/mulberry/sleep_male_,_to.svg
build//symbols/mulberry/wake_up_,_to.svg
build//symbols/mulberry/talk_2_,_to.svg
build//symbols/mulberry/shout_,_to.svg
build//symbols/mulberry/bring_,_to.svg
build//symbols/mulberry/move_,_to.svg
build//symbols/mulberry/fall_over_,_to.svg
build//symbols/mulberry/stand_,_to.svg
build//symbols/mulberry/sit_,_to.svg
build//symbols/mulberry/share_,_to.svg
build//symbols/mulberry/carry_,_to.svg
build//symbols/mulberry/reach_for_,_to.svg
build//symbols/mulberry/hold_,_to.svg
build//symbols/mulberry/keep_,_to.svg
build//symbols/mulberry/jump_,_to.svg
build//symbols/mulberry/chase_,_to.svg
build//symbols/mulberry/climb_up_,_to.svg
build//symbols/mulberry/crawl_,_to.svg
build//symbols/mulberry/hop_,_to.svg
build//symbols/mulberry/enter_door_,_to.svg
build//symbols/mulberry/exit_door_,_to.svg
build//symbols/mulberry/rest_,_to.svg
build//symbols/mulberry/arrest_,_to.svg
build//symbols/mulberry/find_,_to.svg
build//symbols/mulberry/kick_ball_,_to.svg
build//symbols/mulberry/study_,_to.svg
build//symbols/mulberry/change_mind_,_to.svg
build//symbols/mulberry/pray_,_to.svg
build//symbols/mulberry/open_,_to.svg
build//symbols/mulberry/house.svg
build//symbols/mulberry/shop.svg
build//symbols/mulberry/bank.svg
build//symbols/mulberry/office_block.svg
build//symbols/mulberry/outside.svg
build//symbols/mulberry/beach.svg
build//symbols/mulberry/gym_1.svg
build//symbols/mulberry/church.svg
build//symbols/mulberry/field.svg
build//symbols/mulberry/back_garden.svg
build//symbols/mulberry/surgery_health_centre.svg
build//symbols/mulberry/garage.svg
build//symbols/mulberry/aquarium.svg
build//symbols/arasaac/countries.png
build//symbols/mulberry/flag_argentina.svg
build//symbols/mulberry/flag_israel.svg
build//symbols/mulberry/flag_united_states_of_america.svg
build//symbols/mulberry/flag_india.svg
build//symbols/mulberry/flag_united_kingdom.svg
build//symbols/mulberry/flag_france.svg
build//symbols/mulberry/flag_spain.svg
build//symbols/mulberry/flag_indonesia.svg
build//symbols/mulberry/flag_russian_federation.svg
build//symbols/mulberry/flag_poland.svg
build//symbols/mulberry/flag_brazil.svg
build//symbols/mulberry/flag_canada.svg
build//symbols/mulberry/flag_germany.svg
build//symbols/mulberry/flag_lebanon.svg
build//symbols/mulberry/flag_jordan.svg
build//symbols/mulberry/flag_syria.svg
build//symbols/mulberry/flag_egypt.svg
build//symbols/mulberry/flag_iraq.svg
build//symbols/mulberry/flag_italy.svg
build//symbols/mulberry/flag_sweden.svg
build//symbols/mulberry/flag_the_netherlands.svg
build//symbols/mulberry/flag_china.svg
build//symbols/arasaac/it_is.png
build//symbols/mulberry/shapes.svg
build//symbols/mulberry/ugly.svg
build//symbols/mulberry/pretty.svg
build//symbols/mulberry/large.svg
build//symbols/mulberry/little.svg
build//symbols/mulberry/same.svg
build//symbols/mulberry/old_object.svg
build//symbols/mulberry/fast_2.svg
build//symbols/mulberry/dirty.svg
build//symbols/mulberry/quiet.svg
build//symbols/mulberry/loud.svg
build//symbols/mulberry/fat.svg
build//symbols/mulberry/thin.svg
build//symbols/mulberry/tall.svg
build//symbols/mulberry/short_2.svg
build//symbols/mulberry/long.svg
build//symbols/mulberry/empty.svg
build//symbols/mulberry/full.svg
build//symbols/mulberry/deep.svg
build//symbols/mulberry/shallow.svg
build//symbols/mulberry/open_2.svg
build//symbols/mulberry/closed.svg
build//symbols/mulberry/heavy.svg
build//symbols/mulberry/light.svg
build//symbols/mulberry/broken.svg
build//symbols/mulberry/soft.svg
build//symbols/mulberry/hard.svg
build//symbols/mulberry/curly.svg
build//symbols/mulberry/thick.svg
build//symbols/mulberry/shiny.svg
build//symbols/mulberry/fancy.svg
build//symbols/mulberry/noisy.svg
build//symbols/mulberry/dry.svg
build//symbols/mulberry/wet_1.svg
build//symbols/mulberry/sticky.svg
build//symbols/arasaac/i_love.png
build//symbols/mulberry/where.svg
build//symbols/arasaac/my.png
build//symbols/mulberry/teddy_bear.svg
build//symbols/mulberry/doll.svg
build//symbols/mulberry/shape_puzzle.svg
build//symbols/mulberry/toy_car.svg
build//symbols/mulberry/toy_soldier.svg
build//symbols/mulberry/toy_telephone.svg
build//symbols/mulberry/bricks.svg
build//symbols/mulberry/ball.svg
build//symbols/mulberry/bubbles.svg
build//symbols/mulberry/kite.svg
build//symbols/mulberry/playdough.svg
build//symbols/mulberry/puppet.svg
build//symbols/mulberry/beads.svg
build//symbols/mulberry/lego.svg
build//symbols/mulberry/trampoline.svg
build//symbols/mulberry/colouring_book.svg
build//symbols/mulberry/toy_box.svg
build//symbols/mulberry/stickers.svg
build//symbols/mulberry/help_,_to.svg
build//symbols/arasaac/my
build//symbols/mulberry/fork.svg
build//symbols/mulberry/knife.svg
build//symbols/mulberry/spoon.svg
build//symbols/mulberry/plate.svg
build//symbols/mulberry/glass_,_drinking.svg
build//symbols/mulberry/mug_2.svg
build//symbols/mulberry/serviette.svg
build//symbols/mulberry/bowl.svg
build//symbols/mulberry/place_mat.svg
build//symbols/mulberry/cooker.svg
build//symbols/mulberry/fridge.svg
build//symbols/mulberry/apron.svg
build//symbols/mulberry/computer_2.svg
build//symbols/mulberry/laptop.svg
build//symbols/mulberry/electric_charger.svg
build//symbols/mulberry/battery_2.svg
build//symbols/mulberry/camera.svg
build//symbols/mulberry/headphones.svg
build//symbols/mulberry/playstation.svg
build//symbols/mulberry/usb_stick.svg
build//symbols/mulberry/printer.svg
build//symbols/mulberry/computer_mouse_2.svg
build//symbols/mulberry/ipod.svg
build//symbols/mulberry/iphone.svg
build//symbols/mulberry/stereo.svg
build//symbols/mulberry/dvd_player.svg
build//symbols/mulberry/wii.svg
build//symbols/mulberry/remote_control.svg
build//symbols/mulberry/computer_keyboard.svg
build//symbols/mulberry/extension_lead.svg
build//symbols/mulberry/rain.svg
build//symbols/mulberry/sun.svg
build//symbols/mulberry/snow.svg
build//symbols/mulberry/thunder_storm.svg
build//symbols/mulberry/cloudy.svg
build//symbols/mulberry/autumn.svg
build//symbols/mulberry/winter.svg
build//symbols/mulberry/spring.svg
build//symbols/mulberry/summer.svg
build//symbols/mulberry/potted_plant.svg
build//symbols/mulberry/tree.svg
build//symbols/mulberry/branch.svg
build//symbols/mulberry/leaf.svg
build//symbols/mulberry/tree_trunk.svg
build//symbols/mulberry/grass.svg
build//symbols/mulberry/hedge.svg
build//symbols/mulberry/bush.svg
build//symbols/mulberry/flower.svg
build//symbols/mulberry/daffodil.svg
build//symbols/mulberry/daisy.svg
build//symbols/mulberry/rose.svg
build//symbols/mulberry/tulip.svg
build//symbols/mulberry/petal.svg
build//symbols/mulberry/seedling.svg
build//symbols/mulberry/seeds.svg
build//symbols/mulberry/stick.svg
build//symbols/mulberry/roots.svg
build//symbols/mulberry/vine.svg
build//symbols/mulberry/holly.svg
build//symbols/mulberry/weeds.svg
build//symbols/mulberry/ivy_2.svg
build//symbols/mulberry/palm_tree.svg
build//symbols/mulberry/dead_plant.svg
build//symbols/mulberry/acorn.svg
build//symbols/mulberry/cactus.svg
build//symbols/mulberry/pine_cone.svg
build//symbols/mulberry/judo.svg
build//symbols/mulberry/tennis.svg
build//symbols/mulberry/cricket.svg
build//symbols/mulberry/baseball_bat.svg
build//symbols/mulberry/badminton.svg
build//symbols/mulberry/golf.svg
build//symbols/mulberry/archery.svg
build//symbols/mulberry/ski_,_to.svg
build//symbols/mulberry/pool_snooker.svg
build//symbols/mulberry/ride_horse_,_to.svg
build//symbols/mulberry/bowling.svg
build//symbols/mulberry/boccia.svg
build//symbols/mulberry/volleyball.svg
build//symbols/mulberry/olympic_rings.svg
build//symbols/mulberry/para_olympic_games.svg
build//symbols/mulberry/olympic_torch_2.svg
build//symbols/mulberry/race_athletics.svg
build//symbols/arasaac/go.png
build//symbols/mulberry/past.svg
build//symbols/mulberry/car.svg
build//symbols/mulberry/bicycle.svg
build//symbols/mulberry/wheelchair.svg
build//symbols/mulberry/motorcycle.svg
build//symbols/mulberry/bus.svg
build//symbols/mulberry/taxi.svg
build//symbols/mulberry/aeroplane.svg
build//symbols/mulberry/helicopter.svg
build//symbols/mulberry/train.svg
build//symbols/mulberry/mini_bus.svg
build//symbols/mulberry/ferry.svg
build//symbols/mulberry/boat.svg
build//symbols/mulberry/tractor.svg
build//symbols/mulberry/skateboard.svg
build//symbols/mulberry/army_tank.svg
build//symbols/mulberry/hot_air_balloon.svg
build//symbols/mulberry/fire_engine.svg
build//symbols/mulberry/spaceship.svg
build//symbols/mulberry/rocket.svg
build//symbols/mulberry/jeep.svg
build//symbols/mulberry/ambulance.svg
build//symbols/mulberry/police_car.svg
build//symbols/mulberry/van.svg
build//symbols/mulberry/lorry.svg
build//symbols/mulberry/refuse_lorry.svg
build//symbols/mulberry/back_ache.svg
build//symbols/mulberry/headache.svg
build//symbols/mulberry/stomach_ache.svg
build//symbols/mulberry/toothache.svg
build//symbols/mulberry/inhaler.svg
build//symbols/mulberry/rash.svg
build//symbols/mulberry/operation.svg
build//symbols/mulberry/plaster.svg
build//symbols/mulberry/medicine.svg
build//symbols/mulberry/xray.svg
build//symbols/mulberry/syringe.svg
build//symbols/mulberry/tablets.svg
build//symbols/mulberry/blood_pressure.svg
build//symbols/mulberry/cut.svg
build//symbols/mulberry/oxygen_mask.svg
build//symbols/mulberry/vomit_,_to.svg
build//symbols/mulberry/thermometer.svg
build//symbols/mulberry/in.svg
build//symbols/mulberry/out.svg
build//symbols/mulberry/on.svg
build//symbols/mulberry/under_1.svg
build//symbols/mulberry/over.svg
build//symbols/mulberry/behind.svg
build//symbols/mulberry/in_front.svg
build//symbols/mulberry/through.svg
build//symbols/mulberry/between.svg
build//symbols/mulberry/up.svg
build//symbols/mulberry/down.svg
build//symbols/mulberry/left.svg
build//symbols/mulberry/right.svg
build//symbols/mulberry/around.svg
build//symbols/mulberry/forwards.svg
build//symbols/mulberry/backwards.svg
build//symbols/mulberry/before.svg
build//symbols/mulberry/after.svg
build//symbols/mulberry/what.svg
build//symbols/mulberry/why.svg
build//symbols/mulberry/how.svg
build//symbols/mulberry/how_many.svg
build//symbols/mulberry/when.svg
build//symbols/mulberry/which.svg
build//symbols/mulberry/grandfather.svg
build//symbols/mulberry/grandmother.svg
build//symbols/mulberry/sister.svg
build//symbols/mulberry/brother.svg
build//symbols/mulberry/daughter.svg
build//symbols/mulberry/son.svg
build//symbols/mulberry/baby.svg
build//symbols/mulberry/fairy.svg
build//symbols/mulberry/ghost.svg
build//symbols/mulberry/elf.svg
build//symbols/mulberry/witch.svg
build//symbols/mulberry/monster.svg
build//symbols/mulberry/tiger.svg
build//symbols/mulberry/elephant.svg
build//symbols/mulberry/giraffe.svg
build//symbols/mulberry/gorilla.svg
build//symbols/mulberry/snake.svg
build//symbols/mulberry/rattle_snake.svg
build//symbols/mulberry/panda.svg
build//symbols/mulberry/hippopotamus.svg
build//symbols/mulberry/bear.svg
build//symbols/mulberry/polar_bear.svg
build//symbols/mulberry/fox.svg
build//symbols/mulberry/lion.svg
build//symbols/mulberry/wolf.svg
build//symbols/mulberry/chimpanzee.svg
build//symbols/mulberry/deer.svg
build//symbols/mulberry/zebra.svg
build//symbols/mulberry/kangaroo.svg
build//symbols/mulberry/bat.svg
build//symbols/mulberry/koala.svg
build//symbols/mulberry/rhinoceros.svg
build//symbols/mulberry/dinosaur.svg
build//symbols/mulberry/cheetah.svg
build//symbols/mulberry/ant_eater.svg
build//symbols/mulberry/antelope.svg
build//symbols/mulberry/chameleon.svg
build//symbols/mulberry/seahorse.svg
build//symbols/mulberry/penguin.svg
build//symbols/mulberry/starfish.svg
build//symbols/mulberry/dolphin.svg
build//symbols/mulberry/seal.svg
build//symbols/mulberry/killer_whale.svg
build//symbols/mulberry/crab.svg
build//symbols/mulberry/goldfish.svg
build//symbols/mulberry/oyster_2.svg
build//symbols/mulberry/shrimp.svg
build//symbols/mulberry/crocodile_2.svg
build//symbols/mulberry/jellyfish.svg
build//symbols/mulberry/walrus.svg
build//symbols/mulberry/tropical_fish.svg
build//symbols/mulberry/koi_carp_fish.svg
build//symbols/mulberry/chair.svg
build//symbols/mulberry/table.svg
build//symbols/mulberry/high_chair.svg
build//symbols/mulberry/rocking_chair.svg
build//symbols/mulberry/coffee_table.svg
build//symbols/mulberry/rug.svg
build//symbols/mulberry/corner_cabinet_2.svg
build//symbols/mulberry/dresser.svg
build//symbols/mulberry/drawer.svg
build//symbols/mulberry/door_2.svg
build//symbols/mulberry/window.svg
build//symbols/mulberry/book_shelf.svg
build//symbols/mulberry/bookcase.svg
build//symbols/mulberry/stool.svg
build//symbols/mulberry/beanbag.svg
build//symbols/mulberry/dining_table.svg
build//symbols/mulberry/curtains.svg
build//symbols/mulberry/single_bed.svg
build//symbols/mulberry/blanket.svg
build//symbols/mulberry/lamp.svg
build//symbols/mulberry/picture.svg
build//symbols/mulberry/toothbrush.svg
build//symbols/mulberry/toothpaste.svg
build//symbols/mulberry/soap.svg
build//symbols/mulberry/towel.svg
build//symbols/mulberry/comb.svg
build//symbols/mulberry/nail_clippers.svg
build//symbols/mulberry/paper_towel.svg
build//symbols/mulberry/sanitary_towel.svg
build//symbols/mulberry/tissues.svg
build//symbols/mulberry/shampoo.svg
build//symbols/mulberry/aftershave_1.svg
build//symbols/mulberry/electric_razor.svg
build//symbols/mulberry/hair_conditioner.svg
build//symbols/mulberry/make_up.svg
build//symbols/mulberry/deodorant.svg
build//symbols/mulberry/toilet_roll.svg
build//symbols/mulberry/hairdryer.svg
build//symbols/mulberry/hair_dye.svg
build//symbols/mulberry/snail.svg
build//symbols/mulberry/beetle.svg
build//symbols/mulberry/honey_bee.svg
build//symbols/mulberry/ant.svg
build//symbols/mulberry/cricket_2.svg
build//symbols/mulberry/moth.svg
build//symbols/mulberry/butterfly.svg
build//symbols/mulberry/fly.svg
build//symbols/mulberry/dragonfly.svg
build//symbols/mulberry/earwig.svg
build//symbols/mulberry/slug.svg
build//symbols/mulberry/wasp.svg
build//symbols/mulberry/beehive.svg
build//symbols/mulberry/bees_nest.svg
build//symbols/mulberry/caterpillar.svg
build//symbols/mulberry/owl.svg
build//symbols/mulberry/vulture.svg
build//symbols/mulberry/seagull.svg
build//symbols/mulberry/dove.svg
build//symbols/mulberry/duck.svg
build//symbols/mulberry/swan.svg
build//symbols/mulberry/robin.svg
build//symbols/mulberry/turkey.svg
build//symbols/mulberry/ostrich.svg
build//symbols/mulberry/bird.svg
build//symbols/mulberry/flamingo.svg
build//symbols/mulberry/peacock.svg
build//symbols/mulberry/cockerel.svg
build//symbols/mulberry/cockatiel.svg
undefined
Total precache size is about 40.4 MB for 977 resources.
build/service-worker.js has been generated with the service worker contents.
Done in 113.08s.
[BUILD] packaging artefact...
[BUILD] done: dist/uc-cboard-1.39.0.tar.gz
[BUILD] checksum: 36f3b51b08645572dd5fc5952b18f0de0581e1cf956ade3789d66229f7c9fa8b  uc-cboard-1.39.0.tar.gz
[BUILD] publishing the GitHub Release is a separate, deliberate step.
```

