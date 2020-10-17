from manimlib.imports import *

# class Anuncio(Scene):
#     def construct(self):
#         hey   = TextMobject("¡Hey!").scale(5)
#         veros = TextMobject("Esperamos veros en el taller de hoy").scale(1.5)
#         web   = TextMobject("\\texttt{https://deiit.ugr.es/taller-git-oct-2020/}").to_edge(DOWN)
#         hora  = TextMobject("19:30").scale(5).shift(UP)
#         logo  = SVGMobject("scenes/Imago_vertical.svg", fill_color=WHITE).scale(3)

#         self.play(Write(hey))
#         self.wait(2)
#         self.play(Transform(hey, veros))
#         self.wait(2)
#         self.play(
#             FadeOut(hey),
#             Write(web)
#         )
#         self.wait()
#         self.play(Write(hora))
#         self.wait(3)
#         self.play(
#             FadeOut(web),
#             FadeOut(hora)
#         )
#         self.play(DrawBorderThenFill(logo), run_time=3)
#         self.wait(5)
#         self.play(FadeOut(logo), run_time=3)
#         self.wait(0.1)

class _01_Git(Scene):
    def construct(self):
        git = TextMobject("git").scale(2.5)

        self.play(Write(git))
        self.wait(0.1)

class _02_Git_Neq_Github(Scene):
    def construct(self):
        git    = TextMobject("git").scale(2.5)
        github = TextMobject("github").scale(2.5).shift(RIGHT * 2)
        neq    = TexMobject("\\neq").scale(2.5).shift(LEFT)

        self.add(git)

        self.play(
            git.shift, LEFT * 3,
            Transform(git.copy(), github)
        )
        self.play(Write(neq))
        self.wait(0.1)

class _03_Configuracion(Scene):
    def construct(self):
        configuracion = TextMobject("\\textsc{Configuración}").scale(2.5)
        git           = TextMobject("git").scale(2.5).shift(LEFT * 3)
        github        = TextMobject("github").scale(2.5).shift(RIGHT * 2)
        neq           = TexMobject("\\neq").scale(2.5).shift(LEFT)

        self.add(
            git,
            github,
            neq
        )

        self.play(
            FadeOut(git),
            FadeOut(github),
            FadeOut(neq)
        )
        self.play(Write(configuracion))
        self.wait(0.1)

class _04_Configuracion_Comandos(Scene):
    def construct(self):
        configuracion = TextMobject("\\textsc{Configuración}").scale(2.5)
        mail          = TextMobject("\\texttt{git config ----global user.email \"usuario@ejemplo.com\"}").shift(DOWN)
        name          = TextMobject("\\texttt{git config ----global user.name \"nombre\"}")

        self.add(configuracion)

        self.play(configuracion.to_edge, UP)
        self.play(
            Transform(configuracion.copy(), name),
            Transform(configuracion.copy(), mail)
        )
        self.wait(0.1)

class _05_Man(Scene):
    def construct(self):
        configuracion = TextMobject("\\textsc{Configuración}").scale(2.5).to_edge(UP)
        manual        = TextMobject("\\textsc{Manual}").scale(2.5)
        mail          = TextMobject("\\texttt{git config ----global user.email \"usuario@ejemplo.com\"}").shift(DOWN)
        name          = TextMobject("\\texttt{git config ----global user.name \"nombre\"}")

        self.add(
            configuracion,
            mail,
            name,
        )

        self.play(
            FadeOut(configuracion),
            FadeOut(mail),
            FadeOut(name),
        )
        self.play(Write(manual))
        self.wait(0.1)

class _06_Man_Git(Scene):
    def construct(self):
        man    = TextMobject("\\texttt{man git}").scale(2).to_edge(LEFT)
        manual = TextMobject("\\textsc{Manual}").scale(2.5)

        self.add(manual)

        self.play(
            manual.to_corner, UP + RIGHT,
            Transform(manual.copy(), man)
        )
        self.wait(0.1)

class _07_Man_Git_Many(Scene):
    def construct(self):
        manual = TextMobject("\\textsc{Manual}").scale(2.5).to_corner(UP + RIGHT)
        man    = TextMobject("\\texttt{man git}", "\\quad").scale(2).to_edge(LEFT)
        man_   = TextMobject("\\texttt{man git-}", "\\quad").scale(2).to_edge(LEFT)
        init   = TextMobject("init").scale(0.5).next_to(manual, DOWN).to_edge(RIGHT)

        man_git = VGroup(man_)
        names   = VGroup(init)

        def AddMan(*strings):
            for i in strings:
                man_git.add(
                    TextMobject(
                        "\\texttt{man git-}",
                        f"\\texttt{{{i}}}"
                    ).scale(2).to_edge(LEFT)
                )

        def AddName(*strings):
            last = 0
            for i in strings:
                names.add(
                    TextMobject(f"{i}").scale(0.5).next_to(names[last], DOWN).to_edge(RIGHT)
                )
                last += 1

        AddMan(
            "init", "status", "add", "restore", "commit", "log", "whatchanged",
            "diff", "remote", "push", "pull", "clone", "checkout", "branch",
            "merge"
        )
        AddName(
            "status", "add", "restore", "commit", "log", "whatchanged", "diff",
            "remote", "push", "pull", "clone", "checkout", "branch", "merge"
        )

        self.add(
            man,
            manual
        )

        self.play(FadeIn(man_))
        self.remove(man)

        for i in range(15):
            self.play(
                Write(names[i]),
                Transform(man_[1], man_git[i+1][1]),
                run_time = 0.5
            )
        self.wait(0.1)

class _08_Git_Init_01(Scene):
    def construct(self):
        manual    = TextMobject("\\textsc{Manual}").scale(2.5).to_corner(UP + RIGHT)
        init      = TextMobject("init").scale(0.5).next_to(manual, DOWN).to_edge(RIGHT)
        git_init  = TextMobject("\\texttt{git init}").scale(2)
        git_revert = TextMobject("\\texttt{man git-merge}").scale(2).to_edge(LEFT)

        names = VGroup(init)

        def AddName(*strings):
            last = 0
            for i in strings:
                names.add(
                    TextMobject(f"{i}").scale(0.5).next_to(names[last], DOWN).to_edge(RIGHT)
                )
                last += 1

        AddName(
            "status", "add", "restore", "commit", "log", "whatchanged", "diff",
            "remote", "push", "pull", "clone", "checkout", "branch", "merge"
        )

        self.add(
            git_revert,
            manual
        )

        for i in range(15):
            self.add(names[i])

        self.play(
            FadeOut(manual),
            FadeOut(names),
            FadeOut(git_revert),
            Write(git_init)
        )
        self.wait(0.1)

class _09_Git_Init_02(Scene):
    def construct(self):
        git_init  = TextMobject("\\texttt{git init}").scale(2)

        self.add(git_init)

        self.play(git_init.to_edge, UP)
        self.wait()
        self.play(Flash(ORIGIN), run_time = 0.5)
        self.wait(0.1)

class _10_Git_Init_03(Scene):
    def construct(self):
        git_init = TextMobject("\\texttt{git init}").scale(2).to_edge(UP)
        gitdir   = TextMobject("\\texttt{.git}").scale(2)

        self.add(git_init)

        self.play(Write(gitdir))
        self.wait(0.1)

class _11_Git_Status_01(Scene):
    def construct(self):
        git_init   = TextMobject("\\texttt{git init}").scale(2).to_edge(UP)
        git_status = TextMobject("\\texttt{git status}").scale(2)
        gitdir     = TextMobject("\\texttt{.git}").scale(2)

        self.add(git_init, gitdir)

        self.play(
            FadeOut(git_init),
            FadeOut(gitdir),
            Write(git_status)
        )
        self.wait(0.1)

class _12_Git_Status_02(Scene):
    def construct(self):
        git_status = TextMobject("\\texttt{git status}").scale(2)
        untracked  = TextMobject("untracked").scale(2).shift(LEFT * 3)
        unstaged   = TextMobject("unstaged" ).scale(2).shift(RIGHT * 3)

        self.add(git_status)

        self.play(
            git_status.to_edge, UP,
            Transform(git_status.copy(), untracked),
            Transform(git_status.copy(), unstaged)
        )
        self.wait(0.1)

class _13_Git_Add(Scene):
    def construct(self):
        git_add    = TextMobject("\\texttt{git add}").scale(2)
        git_status = TextMobject("\\texttt{git status}").scale(2).to_edge(UP)
        untracked  = TextMobject("untracked").scale(2).shift(LEFT * 3)
        unstaged   = TextMobject("unstaged" ).scale(2).shift(RIGHT * 3)

        self.add(
            git_status,
            untracked,
            unstaged
        )

        self.play(
            FadeOut(git_status),
            FadeOut(untracked),
            FadeOut(unstaged),
            Write(git_add)
        )
        self.wait(0.1)

class _14_Git_MV_RM(Scene):
    def construct(self):
        git_add = TextMobject("\\texttt{git add}").scale(2)
        git_mv  = TextMobject("\\texttt{git mv}").scale(2).shift(LEFT * 3)
        git_rm  = TextMobject("\\texttt{git rm}").scale(2).shift(RIGHT * 3)

        self.add(git_add)

        self.play(
            git_add.to_edge, UP,
            Transform(git_add.copy(), git_mv),
            Transform(git_add.copy(), git_rm)
        )
        self.wait(0.1)

class _15_Git_Restore(Scene):
    def construct(self):
        git_add     = TextMobject("\\texttt{git add}").scale(2).to_edge(UP)
        git_restore = TextMobject("\\texttt{git restore ----staged}").scale(2).to_edge(DOWN)
        git_mv      = TextMobject("\\texttt{git mv}").scale(2).shift(LEFT * 3)
        git_rm      = TextMobject("\\texttt{git rm}").scale(2).shift(RIGHT * 3)

        self.add(
            git_add,
            git_mv,
            git_rm
        )

        self.play(
            Transform(git_add.copy(), git_restore),
            Transform(git_mv.copy(), git_restore),
            Transform(git_rm.copy(), git_restore)
        )
        self.wait(0.1)

class _16_Git_Commit_01(Scene):
    def construct(self):
        git_commit  = TextMobject("\\texttt{git commit}").scale(2)
        git_add     = TextMobject("\\texttt{git add}").scale(2).to_edge(UP)
        git_restore = TextMobject("\\texttt{git restore ----staged}").scale(2).to_edge(DOWN)
        git_mv      = TextMobject("\\texttt{git mv}").scale(2).shift(LEFT * 3)
        git_rm      = TextMobject("\\texttt{git rm}").scale(2).shift(RIGHT * 3)

        self.add(
            git_add,
            git_mv,
            git_rm,
            git_restore
        )

        self.play(
            FadeOut(git_add),
            FadeOut(git_mv),
            FadeOut(git_rm),
            FadeOut(git_restore),
            Write(git_commit)
        )
        self.wait(0.1)

class _17_Git_Commit_02(Scene):
    def construct(self):
        git_commit   = TextMobject("\\texttt{git commit}").scale(2)
        git_commit_m = TextMobject("\\texttt{git commit --m <mensaje corto> --m <mensaje largo>}")

        self.add(git_commit)

        self.play(
            git_commit.to_edge, UP,
            Write(git_commit_m)
        )
        self.wait(0.1)

class _18_Git_Commit_03(Scene):
    def construct(self):
        commit     = Dot().scale(3)
        git_commit = TextMobject("\\texttt{git commit}").scale(2).to_edge(UP)
        git_commit_m = TextMobject("\\texttt{git commit --m <mensaje corto> --m <mensaje largo>}")

        self.add(
            git_commit,
            git_commit_m
        )

        self.play(FadeOut(git_commit_m))

        self.play(FadeInFromLarge(commit))
        self.wait(0.1)

class _19_Git_Commit_04(Scene):
    def construct(self):
        commit  = Dot().scale(3)
        commits = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2)
        )

        git_commit = TextMobject("\\texttt{git commit}").scale(2).to_edge(UP)

        tiempo = Arrow(
            commit.get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        self.add(
            git_commit,
            commits[0]
        )

        self.play(
            GrowArrow(tiempo),
            FadeInFromLarge(commits[1])
        )
        self.wait(0.1)

class _20_Git_Commit_Nomenclatura(Scene):
    def construct(self):
        commit  = Dot().scale(3)
        commits = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2)
        )

        git_commit = TextMobject("\\texttt{git commit}").scale(2).to_edge(UP)
        commit_txt = TextMobject("Commit").next_to(commits[0], DOWN)

        tiempo = Arrow(
            commit.get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama = TextMobject("Rama").next_to(tiempo, RIGHT)

        self.add(
            git_commit,
            commits,
            tiempo
        )

        self.play(
            Write(commit_txt),
            Write(commit_txt.copy().next_to(commits[1], DOWN)),
            Write(rama)
        )
        self.wait(0.1)

class _21_Git_Commit_Many(Scene):
    def construct(self):
        commit  = Dot().scale(3)
        commits = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2)
        )

        git_commit = TextMobject("\\texttt{git commit}").scale(2).to_edge(UP)
        commit_txt = VGroup(TextMobject("Commit").next_to(commits[0], DOWN))
        commit_txt.add(commit_txt[0].copy().next_to(commits[1], DOWN))

        tiempo = Arrow(
            commits[0].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama = TextMobject("Rama").next_to(tiempo, RIGHT)

        self.add(
            git_commit,
            commits,
            tiempo,
            commit_txt,
            rama
        )

        self.play(
            FadeOut(rama),
            FadeOut(commit_txt)
        )

        for i in range(50):
            nuevo_tiempo = Arrow(
                commits[0].get_arc_center() + LEFT * 2, RIGHT * 4,
                tip_length=MED_SMALL_BUFF
            ).set_stroke_width_from_length()

            commits.add(commits[i+1].copy())

            self.play(
                FadeInFromLarge(commits[i+2]),
                commits[0:i+2].shift, LEFT * 2,
                ReplacementTransform(tiempo, nuevo_tiempo),
                run_time = (2*i + 1) / ((i+1)**2),
            )

            tiempo = nuevo_tiempo
        self.wait(0.1)

class _22_Git_Commit_Many_Nomenclatura(Scene):
    def construct(self):
        commit        = Dot().scale(3)
        git_commit    = TextMobject("\\texttt{git commit}").scale(2).to_edge(UP)

        rama = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(LEFT * 2),
            commit.copy().shift(LEFT * 4),
            commit.copy().shift(LEFT * 6),
            commit.copy().shift(LEFT * 8)
        )

        head = TextMobject("\\texttt{HEAD}").next_to(rama[1], DOWN)
        headhat = TextMobject("\\texttt{HEAD\\^{}}").next_to(rama[0], DOWN)
        headhathat = TextMobject("\\texttt{HEAD\\^{}\\^{}}").next_to(rama[2], DOWN)
        head3 = TextMobject("\\texttt{HEAD\\~{}3").next_to(rama[3], DOWN)
        head4 = TextMobject("\\texttt{HEAD\\~{}4").next_to(rama[4], DOWN)

        tiempo = Arrow(
            rama[5].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        main = TextMobject("\\texttt{main}").next_to(tiempo, RIGHT)

        rama.add(
            tiempo
        )

        self.add(
            git_commit,
            rama
        )

        self.play(Write(head))
        self.play(Write(headhat))
        self.play(Write(headhathat))
        self.play(Write(head3))
        self.play(Write(head4))
        self.play(Write(main))

        self.wait(0.1)

class _23_Interrogacion(Scene):
    def construct(self):
        commit        = Dot().scale(3)
        git_commit    = TextMobject("\\texttt{git commit}").scale(2).to_edge(UP)
        interrogacion = TextMobject("?").scale(15)

        rama = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(LEFT * 2),
            commit.copy().shift(LEFT * 4),
            commit.copy().shift(LEFT * 6),
            commit.copy().shift(LEFT * 8)
        )

        head = TextMobject("\\texttt{HEAD}").next_to(rama[1], DOWN)
        headhat = TextMobject("\\texttt{HEAD\\^{}}").next_to(rama[0], DOWN)
        headhathat = TextMobject("\\texttt{HEAD\\^{}\\^{}}").next_to(rama[2], DOWN)
        head3 = TextMobject("\\texttt{HEAD\\~{}3").next_to(rama[3], DOWN)
        head4 = TextMobject("\\texttt{HEAD\\~{}4").next_to(rama[4], DOWN)

        tiempo = Arrow(
            rama[5].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        main = TextMobject("\\texttt{main}").next_to(tiempo, RIGHT)

        rama.add(
            tiempo
        )

        self.add(
            git_commit,
            rama,
            head,
            headhat,
            headhathat,
            head3,
            head4,
            main
        )

        self.play(
            FadeOut(git_commit),
            FadeOut(rama),
            FadeOut(head),
            FadeOut(headhat),
            FadeOut(headhathat),
            FadeOut(head3),
            FadeOut(head4),
            FadeOut(main)
        )

        self.play(Write(interrogacion))
        self.wait(0.1)

class _24_Log_Whatchanged(Scene):
    def construct(self):
        interrogacion   = TextMobject("?").scale(15)
        git_log         = TextMobject("\\texttt{git log}").scale(2).shift(UP)
        git_whatchanged = TextMobject("\\texttt{git whatchanged}").scale(2).shift(DOWN)

        self.add(interrogacion)

        self.play(
            Transform(interrogacion.copy(), git_log),
            Transform(interrogacion, git_whatchanged)
        )
        self.wait(0.1)

class _25_Diff(Scene):
    def construct(self):
        git_diff        = TextMobject("\\texttt{git diff}").scale(2)
        git_log         = TextMobject("\\texttt{git log}").scale(2).shift(UP)
        git_whatchanged = TextMobject("\\texttt{git whatchanged}").scale(2).shift(DOWN)

        self.add(
            git_log,
            git_whatchanged
        )

        self.play(
            Transform(git_log, git_diff),
            Transform(git_whatchanged, git_diff)
        )
        self.wait(0.1)

class _26_Remotos(Scene):
    def construct(self):
        git_diff = TextMobject("\\texttt{git diff}").scale(2)
        remotos  = TextMobject("Remotos").scale(5)

        self.add(git_diff)

        self.play(
            FadeOut(git_diff),
            Write(remotos)
        )
        self.wait(0.1)

class _27_Repositorio_Local(Scene):
    def construct(self):
        commit  = Dot().scale(3)
        local   = TextMobject("Local").scale(2).to_edge(UP)
        remotos = TextMobject("Remotos").scale(5)

        rama = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(LEFT * 2),
            commit.copy().shift(LEFT * 4),
            commit.copy().shift(LEFT * 6),
            commit.copy().shift(LEFT * 8)
        )

        tiempo = Arrow(
            rama[5].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama.add(
            tiempo
        )

        self.add(remotos)

        self.play(
            Transform(remotos, local),
            Write(rama)
        )
        self.wait(0.1)

class _28_Repositorio_Remoto(Scene):
    def construct(self):
        commit = Dot().scale(3)
        local  = TextMobject("Local").scale(2).to_edge(UP)
        remoto = TextMobject("Remoto").scale(2).to_edge(UP).shift(RIGHT * 3).set_color(BLUE)

        rama = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(LEFT * 2),
            commit.copy().shift(LEFT * 4),
            commit.copy().shift(LEFT * 6),
            commit.copy().shift(LEFT * 8)
        )

        tiempo = Arrow(
            rama[5].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama.add(
            tiempo
        )

        rama_remota = rama.copy().set_color(BLUE).shift(DOWN * 3)

        self.add(
            local,
            rama
        )

        self.play(
            Transform(local.copy(), remoto),
            local.shift, LEFT * 3,
            Transform(rama.copy(), rama_remota)
        )
        self.wait(0.1)

class _29_Git_Remote_Add(Scene):
    def construct(self):
        commit = Dot().scale(3)
        local  = TextMobject("Local").scale(2).to_edge(UP).shift(LEFT * 3)
        remoto = TextMobject("Remoto").scale(2).to_edge(UP).shift(RIGHT * 3).set_color(BLUE)
        git_remote_add = TextMobject("\\texttt{git remote add <remoto> <dirección>}")

        rama = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(LEFT * 2),
            commit.copy().shift(LEFT * 4),
            commit.copy().shift(LEFT * 6),
            commit.copy().shift(LEFT * 8)
        )

        tiempo = Arrow(
            rama[5].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama.add(
            tiempo
        )

        rama_remota = rama.copy().set_color(BLUE).shift(DOWN * 3)

        self.add(
            local,
            rama,
            rama_remota,
            remoto
        )

        self.play(
            FadeOut(local),
            FadeOut(rama),
            FadeOut(rama_remota),
            FadeOut(remoto),
            Write(git_remote_add)
        )
        self.wait(0.1)

class _30_Git_Remote_Add_Pop(Scene):
    def construct(self):
        git_remote_add = TextMobject("\\texttt{git remote add <remoto> <dirección>}")

        self.add(git_remote_add)

        self.play(git_remote_add.to_edge, UP)
        self.wait()
        self.play(Flash(ORIGIN), run_time = 0.5)
        self.wait(0.1)

class _31_Git_Push(Scene):
    def construct(self):
        git_push       = TextMobject("\\texttt{git push}").scale(2)
        git_remote_add = TextMobject("\\texttt{git remote add <remoto> <dirección>}").to_edge(UP)

        self.add(git_remote_add)

        self.play(Transform(git_remote_add, git_push))
        self.wait(0.1)

class _32_Git_Push_Visual(Scene):
    def construct(self):
        commit   = Dot().scale(3).shift(LEFT * 8)
        git_push = TextMobject("\\texttt{git push}").scale(2)
        local    = TextMobject("Local")
        remoto   = TextMobject("Remoto").set_color(BLUE)

        rama = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(RIGHT * 4),
            commit.copy().shift(RIGHT * 6),
            commit.copy().shift(RIGHT * 8),
            commit.copy().shift(RIGHT * 10)
        )

        tiempo = Arrow(
            rama[0].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama_remota   = rama.copy().set_color(BLUE).shift(DOWN * 3)
        tiempo_remoto = tiempo.copy().set_color(BLUE).shift(DOWN * 3)

        local.next_to(tiempo, RIGHT)
        remoto.next_to(tiempo_remoto, RIGHT)

        self.add(git_push)

        self.play(git_push.to_edge, UP)
        self.play(
            Write(rama),
            Write(tiempo),
            Write(local)
        )
        self.play(
            GrowArrow(tiempo_remoto),
            Write(remoto)
        )
        for i in range(6):
            self.play(Transform(rama[i].copy(), rama_remota[i]), run_time = 0.5)
        self.wait(0.1)

class _33_Git_Pull(Scene):
    def construct(self):
        commit   = Dot().scale(3).shift(LEFT * 8)
        git_pull = TextMobject("\\texttt{git pull}").scale(2).to_edge(UP)
        git_push = TextMobject("\\texttt{git push}").scale(2).to_edge(UP)
        local    = TextMobject("Local")
        remoto   = TextMobject("Remoto").set_color(BLUE)

        rama_remota = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(RIGHT * 4)
        )

        tiempo_remoto = Arrow(
            rama_remota[0].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama   = rama_remota.copy()
        tiempo = tiempo_remoto.copy()

        rama_remota.add(
            commit.copy().shift(RIGHT * 6),
            commit.copy().shift(RIGHT * 8),
            commit.copy().shift(RIGHT * 10)
        )

        rama.add(
            commit.copy().shift(RIGHT * 6),
            commit.copy().shift(RIGHT * 8),
            commit.copy().shift(RIGHT * 10)
        )

        rama_remota.set_color(BLUE).shift(DOWN * 3)
        tiempo_remoto.set_color(BLUE).shift(DOWN * 3)

        local.next_to(tiempo, RIGHT)
        remoto.next_to(tiempo_remoto, RIGHT)

        self.add(git_push)
        self.play(Transform(git_push, git_pull))

        self.play(
            Write(rama_remota),
            Write(tiempo_remoto),
            Write(rama[0:3]),
            Write(tiempo),
            Write(local),
            Write(remoto)
        )

        self.wait()

        for i in range(3,6):
            self.play(Transform(rama_remota[i].copy(), rama[i]), run_time = 0.5)
        self.wait(0.1)

class _34_Git_Clone(Scene):
    def construct(self):
        commit   = Dot().scale(3).shift(LEFT * 8)
        git_pull = TextMobject("\\texttt{git pull}").scale(2).to_edge(UP)
        git_clone = TextMobject("\\texttt{git clone}").scale(2).to_edge(UP)
        local    = TextMobject("Local")
        remoto   = TextMobject("Remoto").set_color(BLUE)

        rama_remota = VGroup(
            commit,
            commit.copy().shift(RIGHT * 2),
            commit.copy().shift(RIGHT * 4)
        )

        tiempo_remoto = Arrow(
            rama_remota[0].get_arc_center(), RIGHT * 4,
            tip_length=MED_SMALL_BUFF
        ).set_stroke_width_from_length()

        rama   = rama_remota.copy()
        tiempo = tiempo_remoto.copy()

        rama_remota.add(
            commit.copy().shift(RIGHT * 6),
            commit.copy().shift(RIGHT * 8),
            commit.copy().shift(RIGHT * 10)
        )

        rama.add(
            commit.copy().shift(RIGHT * 6),
            commit.copy().shift(RIGHT * 8),
            commit.copy().shift(RIGHT * 10)
        )

        rama_remota.set_color(BLUE).shift(DOWN * 3)
        tiempo_remoto.set_color(BLUE).shift(DOWN * 3)

        local.next_to(tiempo, RIGHT)
        remoto.next_to(tiempo_remoto, RIGHT)

        self.add(git_pull)
        self.play(Transform(git_pull, git_clone))

        self.play(
            Write(rama_remota),
            Write(tiempo_remoto),
            Write(remoto)
        )
        self.wait()
        self.play(
            Transform(tiempo_remoto.copy(), tiempo),
            Transform(remoto.copy(), local)
        )

        for i in range(6):
            self.play(Transform(rama_remota[i].copy(), rama[i]), run_time = 0.5)
        self.wait(0.1)

