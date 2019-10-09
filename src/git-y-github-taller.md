# CHARLA GIT 

Este documento recoge toda la información que se dará en la charla sobre Git el 10 de octubre de 2019 a las 19:30.

## 1 - GIT NO ES GITHUB

Git es un gestor de versiones utilizado primariamente desde la terminal pensado para controlar el progreso de un proyecto software entre varios componentes de un equipo y facilitar su desarrollo.

GitHub es una plataforma online que permite gestionar repositorios de forma visual e interactuar con los repositorios de otros usuarios, que comparten su trabajo públicamente.

Aparte de GitHub, existen otros muchos clientes de Git, como GitLab, GitKraken, OpenHub y otros repositorios creados individualmente, como el AUR (Arch User Repository).
Nosotros nos centramos en GitHub porque es donde hemos decidido alojar nuestros [repositorios de apuntes](https://github.com/DEIIT).

## 2 - CONFIGURACIÓN DE GIT

Sigue las instrucciones para descargar git en función de tu sistema operativo:

- **Linux:** Sigue [este enlace](https://git-scm.com/download/linux) y ejecuta en la terminal las órdenes correspondientes a tu distro.
- **OSX:** Sigue [este enlace](https://git-scm.com/download/mac) y sigue las instrucciones de instalación.
- **Windows:** Sigue [este enlace](https://gitforwindows.org/) y sigue las instrucciones de instalación.

Una vez instalado, ejecuta las siguientes órdenes en la terminal:

```sh
# Introduce un nombre de usuario
git config --global user.name "Usuario"
# Introduce un correo de usuario
git config --global user.email "usuario@correo.com"
# Configura la terminal para que muestre colores en el texto
git config --global color.ui auto
```

Tu nombre y correo de usuario son los que te identificarán al actualizar el repositorio.
No tienes que registrarte en ningún sitio, basta con que introduzcas los que te gusten.
Aunque no tienen que ser los de GitHub o la plataforma que utilices, resulta más fácil identificarte si utilizas los mismos credenciales.

## 3 - ÓRDENES GIT

### `git init`

Para empezar a trabajar en un nuevo repositorio creamos una carpeta con el nombre de nuestro proyecto (puede variar) y ejecutamos `git init` dentro de ella.

Esta orden crea un directorio `.git`, que contiene información sobre el estado del repositorio en cada punto del tiempo registrado, e inicializa el repositorio en la rama `master`.

Aunque las trataremos más adelante y no son estrictamente necesarias para la gestión de un repositorio, es importante saber que las ramas son la metáfora visual que utiliza git para expresar la línea de tiempo de las actualizaciones de un repositorio.
Todos los repositorios tienen una rama principal llamada `master`.

Para representar la evolución de un repositorio utilizaremos un gráfico en el que el tiempo se representa como una línea que apunta hacia adelante, el momento actual como `>` y el inicio del repositorio como `O`:

```
      init  ahora
REPO:  O------>
```

### `git status`

Para consultar los ficheros modificados desde la última actualización del repositorio ejecutamos `git status` dentro del mismo.

Esta orden nos muestra un texto similar al siguiente:

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Makefile
	README.md
	src/

nothing added to commit but untracked files present (use "git add" to track)
```

### `git add`

Con la información de la orden anterior podemos elegir los ficheros que queremos añadir al repositorio usando la orden `git add <ficheros>`.

Cada vez que modificamos un fichero se actualizan su fecha y hora de última modificación, por lo que git deja de reconocerlos como pertenecientes al último estado del repositorio (pertenecen a un punto posterior en el tiempo).
Con `git add` nos aseguramos de añadir uno a uno todos los ficheros que queremos actualizar.
Una ventaja de esta orden es que nos permite añadir directorios y su contenido de forma recursiva, por lo que no es necesario añadir uno a uno todos los ficheros del mismo directorio si se añade el propio directorio.

### `git mv` y `git rm`

Al igual que git no actualiza ficheros si no se añaden manualmente, los ficheros eliminados o desplazados no se actualizan automáticamente, ya que la versión anterior del fichero antes de estas operaciones sigue estando registrada en el repositorio.
Esto quiere decir que, por mucho que se borre un fichero, su inexistencia actual no es suficiente para eliminarlo: hay que hacerlo manualmente.

La orden `git mv`, al igual que la orden POSIX `mv`, nos permite renombrar y desplazar ficheros a lo largo del repositorio y que estos movimientos queden registrados en él. Igualmente, `git rm`, al igual que la orden POSIX `rm`, nos permite eliminar ficheros del repositorio.

**¡ATENCIÓN!: Estas órdenes tienen efectos tangibles sobre los ficheros del repositorio.
Borrarlos o desplazarlos con estas órdenes borrará o desplazará los ficheros del directorio.**

### `git restore`

Al añadir ficheros para la siguiente actualización del repositorio pasan a estar en estado **staged** (¿escenificado?).
Esto quiere decir que, hasta que no se haga efectiva la actualización, los cambios sobre estos ficheros están meramente en consideración para ella.

Si decidiéramos que no queremos añadir algunos de los ficheros a la siguiente actualización, podemos usar la orden `git restore --staged <ficheros>` para no incluirlos pero que conserven los cambios:

```sh
git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   este_no
#         new file:   este_si

git restore --staged este_no

git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   este_si
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         este_no

ls -a
# .  ..  este_no  este_si  .git
```

### `git commit`

Una vez estamos seguros de que hemos incluido los ficheros que queremos actualizar utilizamos la orden `git commit -m "Mensaje de actualización" -m ["Descripción de la actualización"]` para hacer efectivos estos cambios.
Como puedes ver, esta orden admite dos cadenas de caracteres:

- **Mensaje de actualización:** Un mensaje corto (por convención 50 o menos caracteres) sobre los cambios realizados.
- **Descripción de la actualización:** Un bloque de texto opcional en el que se explican detalladamente los cambios realizados.

```sh
git commit -m "[META] Actualizados Makefile y .gitignore" -m "Añadida legibilidad al Makefile y añadidos ficheros a ignorar en el .gitignore."
```

Una vez realizado el *commit*, lo que hasta ahora hemos llamado *actualización* para no dificultar la lectura, sus cambios se guardan en el registro de commits, que veremos más adelante.

Añadido el commit `A`, el repositorio quedaría así:

```
      init   ahora
REPO:  O---A--->
```

El último commit realizado (`A` en este caso) recibe el nombre de `HEAD`.

**¡ATENCIÓN!: Deshacer estos cambios es muy difícil, mucho más trabajando con un repositorio remoto (ver siguiente apartado).
Elige muy bien qué cambios quieres dejar reflejados en tus commits.**

### `git log`

Según vamos realizando commits, éstos se van guardando en el fichero `.git` para registrar la evolución del repositorio.

Si ejecutamos `git log` accedemos una interfaz en la que podemos leer los commits realizados hasta el momento:

```
commit 9d0431253c006222eaae2412c5d4ae065dc7449a
Author: Usuario <usuario@correo.com>
Date:   Wed Oct 9 13:06:49 2019 +0200

    A
```

Navegamos esta interfaz con las teclas de dirección, `j` y `k` o `Av Pág` y `Re Pág` y la cerramos con `q`.

Como puedes ver, el commit realmente no tiene el nombre que le ponemos, sino un *hash* larguísimo.
Éste es un identificador único con el cual nos referimos inequívocamente a cada uno de los commits.
Por lo general, nos basta con usar únicamente los siete primeros números para ello.

### `git whatchanged`

Mientras que `git log` nos muestra únicamente el título y fecha y hora de los commits que se han realizado hasta ahora, no nos muestra los cambios realizados.

Para ello usamos la orden `git whatchanged [commit]`, que nos permite ver qué cambios se han realizado hasta el commit `commit` (inclusive) o hasta el presente.

```
commit 9d0431253c006222eaae2412c5d4ae065dc7449a
Author: Usuario <usuario@correo.com>
Date:   Wed Oct 9 13:06:49 2019 +0200

    A

:000000 100644 0000000 e69de29 A        README.md
```

En este caso se nos indica que se ha creado el fichero `README.md`.
La letra a la derecha del nombre del fichero nos indica el cambios que se ha realizado:

- `A`: Creado (added).
- `D`: Eliminado (deleted).
- `M`: Modificado (modified).

### `git diff`

Con `git log` y `git whatchanged` podemos ver qué ficheros se han cambiado en cada commit. Pero. ¿cuáles han sido estos cambios?

La orden `git diff <commit_inicio> [commit_fin]` nos permite ver qué cambios se han realizado desde `commit_inicio` hasta `commit_fin`.
Si no se especifica `commit_fin`, éste será `HEAD`.

Estos cambios vienen fichero por fichero en verde si representan una adición y en rojo si representan una eliminación.

### `git remote`

Hasta ahora hemos estado trabajando con un repositorio **local**, pero el potencial de git se aprovecha completamente al trabajar con un repositorio **remoto**.

Para asociar nuestro local a un remoto utilizamos la orden `git remote add origin <url>`, siendo `origin` el alias que le damos al remoto por convención.
Es imperativo que el remoto esté inicializado antes de intentar realizar esta acción, pues no funcionará de otra manera.

Al crear un repositorio en GitHub, que no es más que crear un alojamiento para un remoto, se nos indica que, para enlazar nuestro local al remoto, debemos usar `git remote add` seguido de la url del remoto que acabamos de crear.

### `git push`

Las actualizaciones que hacemos en nuestro local no quedan registradas automáticamente en el remoto: tenemos que enviarlas nosotros mismos.

Para enviar una actualización al remoto usamos la orden `git push <remoto> <rama>`.
Como aún no hemos explicado las ramas, estamos trabajando desde y enviando hacia la rama `master`.
Por tanto, la orden que debemos ejecutar para actualizar el remoto es `git push origin master`, que sincroniza la rama `master` del remoto con nuestra rama `master` local.

Por ejemplo, supongamos que hemos añadido un remoto pero aún no hemos hecho push desde el local a los commits `A`, `B` y `C`.
El estado de ambos sería el siguiente:

```
        init           ahora
REMOTO:  O--------------->

 LOCAL:  O---A---B---C--->
```

Si hacemos push, el estado cambiaría al siguiente:

```
        init           ahora
REMOTO:  O---A---B---C--->

 LOCAL:  O---A---B---C--->
```

Con este gráfico podemos apreciar dos cosas muy importantes:

- El repositorio no almacena el momento en el que se hace push, pues el dato relevante en ese caso sería la fecha y hora del último commit.
- El remoto no actualiza los commits a la fecha y hora del push, sino que los almacena de igual forma que en el local, pues no es más que una copia remota del repositorio.

### `git pull`

De la misma forma que podemos *empujar* los cambios al remoto, podemos *tirar* de ellos a nuestro local.

Si queremos actualizar cambios del remoto que se han hecho a partir de otro local, utilizamos `git pull` para sincronizar nuestro local con la versión más reciente de **todo** el remoto.

Por ejemplo, veamos el gráfico anterior considerando un nuevo local en otra máquina.
Para esto, llamaremos `LOCAL1` a lo que antes llamamos `LOCAL` y `LOCAL2` al nuevo local:

```
        init               ahora
REMOTO:  O---A---B---C---D--->

LOCAL1:  O---A---B---C------->

LOCAL2:  O---A---B---C---D--->
```

Como podemos ver, `LOCAL2` ha hecho el commit `D` y push a `master`, por lo que el remoto está actualizado con su local, pero no con el de `LOCAL1`.
Para subsanar esto, `LOCAL1` hace pull antes de sentarse a trabajar y el estado de los repositorios pasaría a ser el siguiente:

```
        init               ahora
REMOTO:  O---A---B---C---D--->

LOCAL1:  O---A---B---C---D--->

LOCAL2:  O---A---B---C---D--->
```

Ahora `LOCAL1` puede ponerse a trabajar conociendo todos los cambios realizados por `LOCAL2`.

### `git clone`

En el apartado anterior, `LOCAL2` tenía una copia local del repositorio sincronizada con el remoto. ¿Cómo la ha conseguido?

Para crear una copia local de un remoto utilizamos la orden `git clone <url>.git [directorio]`.
Si no especificamos un directorio en el que clonar el repositorio, se clona en el directorio de trabajo actual.

### `git checkout`

Al trabajar con un repositorio podemos tener varias ramas de desarrollo.
La utilidad de tener diferentes ramas es que se pueden dividir las actividades a realizar sobre los ficheros de forma exclusiva.
Por ejemplo, podemos tener una rama `dev` para cambios inestables.

Para crear una rama usamos la orden `git checkout -b <rama>`.
Esto nos crea la rama que queremos y nos cambia automáticamente a ella.

Tomemos como ejemplo un repositorio en el que `master`, la única rama que lo compone, tiene dos commits `A` y `B`:

```
      init       ahora
REPO:  O---A---B--->
```

Ahora hacemos `git checkout -b dev` para crear la rama `dev` y hacemos en ella un commit `C`:

```
              init
REPO: master:  O---A---B----->
                        \  ahora
                   dev:  C--->
```

Con este gráfico podemos apreciar dos cosas muy importantes:

- La rama no aparece en un punto dedicado del tiempo, sino justo después del último commit realizado, ya que no importa si la rama se hizo justo después o pasado un mes si no hay más commits.
- La rama va de un commit a otro, pues lo normal es crearla para hacer commit sobre ella, aunque se puede crear una rama sin hacer commits.

Un ejemplo de una rama sin commits sería una que hiciera una *snapshot* fácilmente accesible en un momento del tiempo:

```
              init
REPO: master:  O---A---B---C---D--->
                        \        ahora
                  2019:  x
                        fin
```

### `git branch`

Para consultar la lista de ramas que componen un repositorio podemos usar la orden `git branch`, que nos devuelve una lista de todas las ramas marcando la nuestra con un `*`.

Para eliminar una rama usamos la orden `git branch -d <rama>`.
Tomemos como ejemplo el gráfico del apartado anterior:

```
              init
REPO: master:  O---A---B----->
                        \  ahora
                   dev:  C--->
```

Si eliminásemos la rama tras el commit `C`, éste sería el estado del repositorio:

```
              init
REPO: master:  O---A---B----->
                        \  ahora
                   dev:  Cx
                         fin
```

Esto no elimina los cambios realizados sobre la rama antes de realizar la eliminación, sólo deja de registrar cambios sobre ella y mostrarla como rama activa.

### `git switch`

Para cambiar de rama utilizamos `git switch <rama>`, siendo `<rama>` una rama ya existnte.
De esta forma podemos hacer commits en ambas ramas.

Por ejemplo, supongamos que tenemos el repositorio del apartado anterior:

```
              init
REPO: master:  O---A---B----->
                        \  ahora
                  *dev:  C--->
```

Como puedes ver, nos encontramos en la rama `dev`.
Si hacemos un commit `D` en `dev`, `git switch master` y un commit `E`, quedaría así:

```
               init
REPO: *master:  O---A---B---------E--->
                         \          ahora
                    dev:  C---D------->
```

Es importante aprecier que los commits `B` y `E` se han separado para dar espacio a `C` y `D` y crear una sensación de progresión temporal.
Esto es únicamente un detalle de la representación gráfica de ambas ramas, ya que a git no le importa el momento de realización del commit dentro de la propia rama.

### `git merge`

Tras llevar un tiempo trabajando con una rama querremos unir sus cambios a los de `master` o los de otra rama.

Para ello, nos colocamos en la rama que queremos actualizar y ejecutamos `git merge <rama> -m "Mensaje del commit"`.
Aunque se puede hacer merge sin un mensaje de commit, es mejor práctica indicar con uno el momento de unión de ambas ramas para facilitar la navegación a lo largo del repositorio.

Tomemos como ejemplo el siguiente repositorio:

```
               init
REPO: *master:  O---A---B---D----->
                         \      ahora
                    dev:  C---E--->
```

Estando en `master` ejecutamos `git merge dev -m "E"`.
El estado del repositorio pasa a ser el siguiente:

```
               init
REPO: *master:  O---A---B---D---F------>
                         \     /     ahora
                    dev:  C---E-------->
```

Esto nos indica que todos los cambios hechos desde `B` hasta `F` en la rama `dev` ahora están integrados en `master`, no haciendo falta incluirlos en la misma.

De la misma forma, es importante también ver la correlación temporal entre el commit `D` y los commits `C` y `E`.
Aunque en la misma rama git no tiene en cuenta la fecha y hora de los commits, sí los tiene en cuenta si son de diferentes ramas, de forma que sabe que `C` se ha creado antes que `D` y éste antes que `E`:

```
               init
REPO: *master:  O---A---B---D---F------>
                         \| | |/     ahora
                    dev:  C---E-------->
```

### `git rebase`

En contraposición a la unión de dos ramas, podemos hacer un *rebase* (¿recimentación?) de una rama con todos los commits de otra hasta el momento.

Colocándonos en la rama sobre la que queremos hacer rebase, ejecutamos `git rebase <rama>` para unir todos los commits realizamos en la rama `rama` a la nuestra previo a todos los commits de la rama actual que no se han unido a la rama `rama`.
Es más fácil verlo visualmente:

```
              init
REPO: master:  O---A---B---D----->
                        \      ahora
                  *dev:  C---E--->
```

Encontrándonos en la rama `dev`, ejecutamos `git rebase master`:

```
              init
REPO: master:  O---A---B---D--------->
                            \      ahora
                      *dev:  C'--E'-->
```

En la representación gráfica, los commits `C` y `E` pasan a ser `C'` y `E'` respectivamente.
En la realidad, los commits no varían su contenido, pero sí el contenido ajeno a ellos con el que trabajan (como puede ser la mejora de un algoritmo que no se ha modificado en ellos).

Ejecutando `git log` podemos ver que, aunque las fechas no coinciden en el orden cronológico, el orden de los commits coincide con el del gráfico:

```
commit 71c9c8bf989189668237a9abfb7b58da5eb72f48 (HEAD -> dev)
Author: Usuario <usuario@correo.com>
Date:   Wed Oct 9 18:53:47 2019 +0200

    E

commit 65c35a92220ff7a8f1bbf59841621ec69e3689d2 (master)
Author: Usuario <usuario@correo.com>
Date:   Wed Oct 9 18:54:01 2019 +0200

    D

commit 26767459e2fde0d3f9dd3b04be4991249e14a8c2
Author: Usuario <usuario@correo.com>
Date:   Wed Oct 9 18:51:30 2019 +0200

    C
```

Ten en cuenta que, en el log, los commits `C'` y `E'` aparecen como `C` y `E` respectivamente.

### `git fetch`

Al hacer pull desde un remoto, git descarga los commits que han de actualizarse y hace merge a las ramas correspondientes.

Para evitar hacer merge y simplemente consultar los cambios realizados sin actualizar nuestro repositorio usamos la orden `git fetch [rama]`.
Por defecto, `git fetch` descarga todos los commits de `origin`.

Tras descargar los commits, se muestran con el prefijo `* [new tag]`, permitiéndonos ejecutar `git log` sobre ellos.

### `git revert`

Si se han cometido errores en los últimos commits, lo más sensato es borrar todos los ficheros que hemos añadido y hacer un commit que vuelva al estado anterior.
Sin embargo, es posible que haya ficheros que se hayan actualizado a trozos y esta acción consuma demasiado tiempo.

La orden `git revert <commit> -m "Mensaje del commit"` nos permite realizar un commit en el que se vuelva al estado en el que estaba el repositorio justo tras realizar el commit `commit`.

## 3 - FUNCIONES DE GITHUB

### Crear un remoto

Para crear un remoto en GitHub podemos ir a la pantalla de inicio o a nuestra lista de repositorios y pulsar el botón de **new** en verde.
Al crear un repositorio GitHub nos varias elecciones:

**Público o privado:** Los repositorios con un remoto público son visibles para todo el mundo y los privados, sólo por quienes tengan permisos de colaboración.

**Crear README.md:** Inicializa el repositorio con un fichero `README.md` que contiene el título del mismo.

**Crear .gitignore:** Inicializa el repositorio con un fichero `.gitignore`.

Lo ideal es no inicializar el repositorio desde GitHub y hacerlo desde la terminal.
Si no seleccionamos ninguno de los dos últimos ficheros, GitHub nos dará instrucciones para añadir un remoto a nuestro local (las mismas que vimos anteriormente).

### Gestionar un remoto

En un primer vistazo, GitHub nos permite ver el número de commits, ramas, releases, contibutores y la licencia de nuestro repositorio; así como acceder a las issues y pull request (que veremos más adelante), los proyectos (que son una plataforma de [SCRUM](https://en.wikipedia.org/wiki/Scrum_(software_development)), la wiki y las opciones del repositorio.

La wiki es una página en la que se puede (y debe) escribir documentación sobre el repositorio, sus usos, funciones y todo aquello que facilite el trabajo con el mismo.

Las opciones nos permiten cambiar el nombre y opciones básicas del remoto (incluso eliminarlo), añadir colaboradores y formar equipos, agregar integración con servicios de terceros y gestionar la protección de las ramas.
Esta protección permite a los adminsitradores del repositorio crear restricciones para que los cambios de otros usuarios no puedan ser aceptados sin consenso del equipo.

### Issues

Si te encuentras con un problema al utilizar el contenido de un repositorio puedes enviar una issue explicando dicho problema de forma detallada.
Tras esto, un administrador del repositorio comenzará una discusión pública contigo tanto para ayudarte a solventarla como para arreglar aquello que te está causando el problema.

Muchos repositorios incorporan secciones específicas en el apartado de issues para gestionar más ágilmente a qué se refiere cada una y poder asignar así qué adminsitrador se ocupa de resolverlas.

### Fork

Para trabajar con un repositorio es imperativo tener acceso de colaboración al mismo.
¡Imagina el caos que crearía que todo el mundo pudiera escribir en [el repositorio de Linux](https://github.com/torvalds/linux)!
Para poder editar un repositorio ajeno creamos una copia propia mediante un fork (bifurcación).

Podemos hacer esto desde el botón "fork" que se encuentra arriba a la derecha en la página principal del repositorio.
Esto crea una copia del repositorio en un remoto a nuestro nombre.
Es equivalente a clonar el repositorio y cambiar el remoto a uno nuestro.

Una vez hecho nuestro fork, podemos clonarlo y trabajar sobre él como queramos, actualizando a nuestro remoto cuando queramos.
Para añadir nuestros cambios al repositorio original creamos una pull request.

### Pull Request

Una vez hayamos hecho los cambios que queremos en nuestro fork del repositorio, pulsamos el botón "pull request" de la página principal de nuestro fork para iniciar una Pull Request o PR.

Tras iniciar la PR, los administradores del repositorio original comprobarán que tus cambios sean viables para introducirlos en el repositorio original y te indicarán si debes hacer modificaciones al contenido de tu PR.
Una vez sea aceptada, harán merge de tu PR con el repositorio original y tus cambios se verán reflejados en el repositorio original.

## 4 - MALAS PRÁCTICAS

A la hora de añadir ficheros al repositorio para el siguiente commit, ejecutar la orden `git add .` sin comprobar previamente qué se está actualizando con `git status` puede (muy probablemente) añadir al repositorio ficheros actualizados parcialmente que no están listos para ser registrados.

En proyectos muy grandes y complejos es mala práctica hacer push a `master` directamente.
Lo ideal es crear una rama de desarrollo sobre la que ir registrando commits y hacer merge sobre `master` cuando se quiera avanzar una aversión en ella, ya que debe ser la rama de actualizaciones estables.
